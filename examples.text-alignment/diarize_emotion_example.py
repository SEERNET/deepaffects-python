from deepaffects.realtime.util import get_deepaffects_client, chunk_generator_from_file, chunk_generator_from_url
import m3u8
from pprint import pprint
from pytube.compat import urlopen
from pydub import AudioSegment
import io
import time
import os
import pprint
import sys
import json
from deepaffects.realtime.util import get_segment_chunk_from_pydub_chunk
from protobuf_to_dict import protobuf_to_dict

TIMEOUT_SECONDS = 100000
apikey = ""
file_path = "/Users/VivekNimkarde/DeepAffects/my_files/TSLA-q1-2018.mp3"
is_youtube_url = False
languageCode = "en-Us"
sampleRate = "16000"
encoding = "mp3"
window = "5"
threshold = "0.05"
apiVersion = "v2"
verbose = "True"
doVad = "False"
speakerIds = "TSLA_Deepak_Ahuja_v2,TSLA_Elon_Musk_v2,TSLA_Jeff_Evanson_v2,TSLA_Jeffrey_Straubel_v2,TSLA_Martin_Viecha_v2"
chunk = None

# DeepAffects realtime Api client
client = get_deepaffects_client("dev-realtime.deepaffects.com:80")

metadata = [
    ('apikey', apikey),
    ('encoding', encoding),
    ('samplerate', sampleRate),
    ('languagecode', languageCode),
    ('speakerids', speakerIds),
    ('window', window),
    ('threshold', threshold),
    ('dovad', doVad),
    ('apiversion', apiVersion),
    ('verbose', verbose)
]

# Implement chunk_generator() is a generator function which yields segment_chunk objects asynchronously
# from deepaffects.realtime.types import segment_chunk
# yield segment_chunk(Args)
"""segment_chunk.

Args:
    encoding : Audio Encoding,
    languageCode: language code ,
    sampleRate: sample rate of audio ,
    content: base64 encoded audio,
    segmentOffset: offset of the segment in complete audio stream
"""

"""
Sample implementation which reads audio from a file and splits it into
segments more than 3 sec
AudioSegment and yields base64 encoded audio segment objects asynchronously
"""

"""Stream audio from earningcast.
"""
resparr = []

try:
    responses = client.DiarizeEmotion(
    chunk_generator_from_file(file_path), TIMEOUT_SECONDS, metadata=metadata)

    # responses is the iterator for all the response values
    for response in responses:
        print("Received messager")
        # print(response)
        print(response)
        dict_resp = protobuf_to_dict(response)
        if "start" not in dict_resp:
            dict_resp["start"] = 0
        resparr.append(dict_resp)
        # print(json.dumps(dict_resp))
finally:    
    with open("examples.text-alignment/diarization_output.json", 'w') as outfile:
        json.dump(resparr, outfile)
    

# responses is the iterator for all the response values

"""Response.
    response = {
        emotion: Emotion identified in the segment,
        start: start of the segment,
        end: end of the segment
    }
"""
