const puppeteer = require("puppeteer");
var fs = require("fs");
let textArrays = [];
let startWriting = true;
let Datajson = [];
const checkQuarter = function(text, quarters) {
  for (const quarter of quarters) {
    if (text.includes(quarter)) {
      return true;
    }
  }
};
const getFileName = function(company, link) {
  for (const quarter of company.quarters) {
    if (link.includes(quarter)) {
      return company.name + "-" + quarter;
    }
  }
};

async function run() {
  const browser = await puppeteer.launch({
    executablePath:
      "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    headless: false,
    args: ["--no-sandbox", "--disable-setuid-sandbox"]
  });
  const page = await browser.newPage();
  page.setViewport({ width: 1280, height: 926 });

  const companies = [
    { name: "TSLA", quarters: ["q1-2018"] }
    // { name: "IONS", quarters: ["q1-2018"] }
    // { name: "LB", quarters: ["q1-2018"] }
  ];
  try {
    for (const key in companies) {
      let company = companies[key];
      //   await page.goto(
      //     "https://seekingalpha.com/symbol/" +
      //       company.name +
      //       "/earnings/transcripts"
      //   );
      //   await page.evaluate(async () => {
      //     await new Promise((resolve, reject) => {
      //       try {
      //         const maxScroll = Number.MAX_SAFE_INTEGER;
      //         let lastScroll = 0;
      //         const interval = setInterval(() => {
      //           window.scrollBy(0, 100);
      //           const scrollTop = document.documentElement.scrollTop;
      //           if (scrollTop === maxScroll || scrollTop === lastScroll) {
      //             clearInterval(interval);
      //             resolve();
      //           } else {
      //             lastScroll = scrollTop;
      //           }
      //         }, 100);
      //       } catch (err) {
      //         console.log(err);
      //         reject(err.toString());
      //       }
      //     });
      //   });

      //   let links = await page.evaluate(() => {
      //     return Array.from(document.querySelectorAll("a"))
      //       .filter(val => val.text.includes("Earnings Call Transcript"))
      //       .map(val => val.href);
      //   });

      let links = [
        "https://seekingalpha.com/article/4165994-ford-motor-f-q1-2018-results-earnings-call-transcript"
        // "https://seekingalpha.com/article/4170131-ionis-pharmaceuticals-ions-ceo-stan-crooke-q1-2018-results-earnings-call-transcript"
        // "https://seekingalpha.com/article/4176910-l-brands-inc-lb-ceo-martin-waters-q1-2018-results-earnings-call-transcript"
      ];

      for (const link of links) {
        console.log(link);
        console.log(checkQuarter(link, company.quarters));
        if (checkQuarter(link, company.quarters)) {
          startWriting = false;
          let madeLink = link + "?part=single";
          console.log(madeLink);
          await page.goto(madeLink);
          //delay
          await page.waitFor(1000);
          let textElements = await page.evaluate(() => {
            return Array.from(document.querySelectorAll("p"))
              .filter(val => {
                console.log(val.innerText);
                if (val.innerText.includes("Operator")) {
                  console.log(this.startWriting, val.innerText);
                  this.startWriting = true;
                }
                return this.startWriting;
              }, this)
              .map(val => {
                return {
                  text: val.innerText,
                  html: val.innerHTML
                };
              });
          });
          textArrays = [];
          copyrightStarted = false;
          console.log(textElements);
          for (const textElement of textElements) {
            if (
              textElement.text.includes(
                "Copyright policy: All transcripts on this site are the copyright of Seeking Alpha"
              )
            ) {
              copyrightStarted = true;
            }
            if (!copyrightStarted) {
              if (textElement.html.includes("<strong>")) {
                speaker = textElement.text;
                type = textElement.html.includes('class="answer"')
                  ? "Answer"
                  : textElement.html.includes('class="question"')
                    ? "Question"
                    : "Statement";
              } else {
                textArrays.push({
                  speaker: speaker,
                  text: textElement.text,
                  type: type
                });
              }
            }
          }
          let callReport = {
            company: company.name,
            callTranscriptLink: madeLink,
            transcript: textArrays
          };
          Datajson.push(callReport);
          fs.writeFile(
            "earning-call-transcripts/" +
              getFileName(company, madeLink) +
              ".json",
            JSON.stringify(callReport),
            error => {
              console.log(error);
            }
          );
        }
      }
    }
  } catch (err) {
    console.log(Datajson);
    fs.writeFile("dump.json", JSON.stringify(Datajson), error => {
      console.log(error);
    });
    browser.close();
  }
}

run();
