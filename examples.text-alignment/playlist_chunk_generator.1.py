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
apikey = "1JtnGOAwHuGwT0wwrDzdSikyUxqc99ZA"
file_path = "http://wowza.earningscast.com:1935/vod/_definst_/mp4:671c25caa2dd54548a89bc76b963ee42.m4a/playlist.m3u8"
is_youtube_url = False
languageCode = "en-Us"
sampleRate = "16000"
encoding = "mp3"
window = "5"
threshold = "0.05"
apiVersion = "v2"
verbose = "True"
doVad = "False"
speakerIds = "CRM_John_Cummings,CRM_Marc_Benioff,CRM_Keith_Block,CRM_Mark_Hawkins,CRM_Bret_Taylor"
chunk = None

def chunk_generator_from_playlist(file_path=None, buffer_size=3):
    try:
        offset = 0
        last_processed = -1
        endlist = False
        # for playlists with m3u8 extensions
        m3u8_obj_outer = m3u8.load(
            file_path)
        base_uri = m3u8_obj_outer.base_uri
        base_audio = m3u8_obj_outer.data['playlists'][0]['uri']
        audio_stream_url = base_uri + base_audio
        chunk_index = 1
        index = 0

        while endlist is not True:
            m3u8_obj = m3u8.load(audio_stream_url)            
            if last_processed < m3u8_obj.media_sequence:                
                for i, segment in enumerate(m3u8_obj.data['segments']):
                    response = urlopen(base_uri + segment['uri'])
                    buff = response.read()
                    if chunk_index == 1:
                        chunk = AudioSegment.from_file(io.BytesIO(buff), "aac")    
                        chunk_index = chunk_index + 1
                    elif chunk_index < buffer_size:
                        chunk = chunk + AudioSegment.from_file(io.BytesIO(buff), "aac")                                            
                        chunk_index = chunk_index + 1
                    elif chunk_index == buffer_size:
                        chunk = chunk + AudioSegment.from_file(io.BytesIO(buff), "aac") 
                        print(offset, len(chunk)/1000)
                        audio_segment, offset = get_segment_chunk_from_pydub_chunk(chunk, offset, index)
                        index = index + 1
                        yield audio_segment                                               
                        chunk_index = 1                                                              
                last_processed = m3u8_obj.media_sequence
                     
            if m3u8_obj.data['is_endlist'] == True:
                endlist = True
            else:
                time.sleep(2)

    except KeyboardInterrupt:
        print('Interrupted Stopping Stream')
        with open("file.wav", "wb") as f:
            chunk.export(f, format="wav")
        os._exit(0)

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
    chunk_generator_from_playlist(file_path), TIMEOUT_SECONDS, metadata=metadata)

    # responses is the iterator for all the response values
    for response in responses:
        print("Received messager")
        # print(response)
        print(response)
        dict_resp = protobuf_to_dict(response)
        if dict["start"] is None:
            dict["start"] = 0
        resparr.append(dict_resp)
        # print(json.dumps(dict_resp))
finally:    
    with open("diarization_output.json", 'w') as outfile:
        json.dump(resparr, outfile)
    

# responses is the iterator for all the response values

"""Response.
    response = {
        emotion: Emotion identified in the segment,
        start: start of the segment,
        end: end of the segment
    }
"""
