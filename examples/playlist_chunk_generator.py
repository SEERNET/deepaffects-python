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

TIMEOUT_SECONDS = 10000
apikey = "YOUR_API_KEY"
file_path = "PLAYLIST_PATH"
is_youtube_url = False
languageCode = "en-Us"
sampleRate = "16000"
encoding = "mp3"
speakerIds = "list of userids for for speaker verification seperated by ','"
apiVersion = "v2"
verbose = "True"


def chunk_generator_from_playlist(file_path=None, buffer_size=30000):
    try:
        offset = 0
        last_processed = -1
        endlist = False
        # for playlists with m3u8 extensions
        m3u8_obj_outer = m3u8.load(file_path)
        base_uri = m3u8_obj_outer.base_uri
        base_audio = m3u8_obj_outer.data['playlists'][0]['uri']
        audio_stream_url = base_uri + base_audio
        chunk_index = 1
        index = 0
        unsent_segment = False
        while endlist is not True:
            m3u8_obj = m3u8.load(audio_stream_url)
            if last_processed < m3u8_obj.media_sequence:
                for i, segment in enumerate(m3u8_obj.data['segments']):
                    response = urlopen(base_uri + segment['uri'])
                    buff = response.read()
                    if chunk_index == 1:
                        chunk = AudioSegment.from_file(io.BytesIO(buff), "aac")
                    else:
                        chunk = chunk + AudioSegment.from_file(io.BytesIO(buff), "aac")
                    offset_in_milliseconds = offset * 1000
                    if (len(chunk) - (offset_in_milliseconds)) > buffer_size:
                        segment_chunk = chunk[offset_in_milliseconds: offset_in_milliseconds + buffer_size]                        
                        audio_segment, offset = get_segment_chunk_from_pydub_chunk(segment_chunk, offset, index)
                        index = index + 1
                        yield audio_segment
                    chunk_index = chunk_index + 1
                if (len(chunk) - (offset * 1000)) != 0:
                    segment_chunk = chunk[offset * 1000:]
                    audio_segment, offset = get_segment_chunk_from_pydub_chunk(segment_chunk, offset, index)
                    index = index + 1
                    yield audio_segment
                last_processed = m3u8_obj.media_sequence

            if m3u8_obj.data['is_endlist'] == True:
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
    ('speakerids', speakerIds),
    ('encoding', encoding),
    ('samplerate', sampleRate),
    ('languagecode', languageCode),
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
responses = client.DiarizeEmotion(
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
