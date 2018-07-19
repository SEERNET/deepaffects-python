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
from deepaffects.realtime.util import get_segment_chunk_from_pydub_chunk

TIMEOUT_SECONDS = 2000
apikey = "Pnpr9E0nEWEdVByJoGxquE7EPjbFLB0W"
file_path = "http://wowza.earningscast.com:1935/vod/_definst_/mp4:4fc5368668748a651d62edefb78ba8a5.m4a/playlist.m3u8"
is_youtube_url = False
languageCode = "en-Us"
sampleRate = "16000"
encoding = "mp3"


def chunk_generator_from_playlist(file_path=None):
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

        while endlist is not True:
            m3u8_obj = m3u8.load(audio_stream_url)
            print(m3u8_obj)
            for i, segment in enumerate(m3u8_obj.data['segments']):
                if last_processed < i:
                    response = urlopen(base_uri + segment['uri'])
                    buff = response.read()
                    chunk = AudioSegment.from_file(io.BytesIO(buff), "aac")
                    audio_segment, offset = get_segment_chunk_from_pydub_chunk(
                        chunk, offset, i)
                    last_processed = i
                    yield audio_segment
            if m3u8_obj.data['is_endlist']:
                endlist = True
            else:
                time.sleep(2)

    except KeyboardInterrupt:
        print('Interrupted Stopping Stream')
        os._exit(0)


# DeepAffects realtime Api client
client = get_deepaffects_client()

metadata = [
    ('apikey', apikey),
    ('encoding', encoding),
    ('samplerate', sampleRate),
    ('languagecode', languageCode)
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
responses = client.IdentifyEmotion(
    chunk_generator_from_playlist(file_path), TIMEOUT_SECONDS, metadata=metadata)

# responses is the iterator for all the response values
for response in responses:
    print("Received message")
    print(response)

"""Response.
    response = {
        emotion: Emotion identified in the segment,
        start: start of the segment,
        end: end of the segment
    }
"""
