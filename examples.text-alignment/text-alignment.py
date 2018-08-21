#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
import sys
import json
from aeneas.tools.execute_task import ExecuteTaskCLI
reload(sys)
sys.setdefaultencoding("utf-8")
file_path = "/Users/VivekNimkarde/DeepAffects/my_files/TSLA-q1-2018.mp3"
transcript_path = "/Users/VivekNimkarde/DeepAffects/deepaffects-python/examples.text-alignment/transcripts/TSLA-q1-2018.json"

# with open(transcript_path) as f:
#     fileData = json.load(f)
#     with open("text_file.txt", "w") as txt:
#         for seg in fileData['transcript']:
#             for word in seg['text'].split(" "):                    
#                 w  = word.encode('utf-8') 
#                 txt.write(w + "\n")
#         txt.close()
#     f.close()
#     # Text Alignment    
# print("Starting align")
# ExecuteTaskCLI(use_sys=False).run(arguments=[
#     None,  # dummy program name argument
#     u"/Users/VivekNimkarde/DeepAffects/my_files/TSLA-q1-2018.mp3",
#     u"text_file.txt",
#     u"task_language=eng|is_text_type=plain|os_task_file_format=json",
#     u"./examples.text-alignment/word-alignment.json"
# ])

with open("./examples.text-alignment/word-alignment.json") as aligned_transcript, open("./examples.text-alignment/diarization_output.json") as diarized_seg , open("./examples.text-alignment/final_output.json", "w") as final_output:
    transcriptjson = json.load(aligned_transcript)
    words = transcriptjson['fragments']
    word_count = len(words)
    segments = json.load(diarized_seg)    
    new_segments = []
    index = 0
    for segment in segments :        
        text = ""        
        while float(words[index]["begin"]) < segment["end"] and float(words[index]["begin"]) >= segment["start"] and index < word_count :
            text = text + words[index]["lines"][0]  + " "    
            index = index + 1;        
        segment["text"] = text
        new_segments.append(segment)
    json.dump(new_segments, final_output)

    

# responses is the iterator for all the response values

"""Response.
    response = {
        emotion: Emotion identified in the segment,
        start: start of the segment,
        end: end of the segment
    }
"""
