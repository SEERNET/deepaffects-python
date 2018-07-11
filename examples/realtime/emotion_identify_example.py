import sys
from pydub import AudioSegment
from random import randint
import time
from deepaffects.realtime.util import get_segment, make_input_audio_segments, encode_to_base64, get_deepaffects_client, audio_segment_to_base64


TIMEOUT_SECONDS = 2000
API_KEY = "YOUR_API_KEY"
file_path = "FILE_PATH"


def chunk_generator():
    # Implement this generator function to yield Audio segments
    # To generate Audio Segments use make_input_audio_segment
    """make_input_audio_segment.

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
    audio_clip = AudioSegment.from_file(file_path)
    offset = None
    previous_chunk = None

    for i, chunk in enumerate(audio_clip[::15500]):

        if offset is None:
            offset = 0

        if previous_chunk is not None:

            if len(chunk) <= 3000:

                previous_chunk = previous_chunk + chunk
                audio_segment, offset = get_segment(previous_chunk, offset, i)
                yield audio_segment

            elif (len(chunk) < 15500) and (len(chunk) > 3000):

                audio_segment, offset = get_segment(previous_chunk, offset, i)
                previous_chunk = chunk
                yield audio_segment
                audio_segment, offset = get_segment(previous_chunk, offset, i)
                yield audio_segment

            else:

                audio_segment, offset = get_segment(previous_chunk, offset, i)
                previous_chunk = chunk
                yield audio_segment

        if previous_chunk is None:
            previous_chunk = chunk


def identify_emotion():

    # DeepAffects realtime Api client
    client = get_deepaffects_client()

    metadata = [('apikey', API_KEY)]

    # chunk_generator() is a generator function which yields audio segment object asynchronously
    responses = client.IdentifyEmotion(
        chunk_generator(), TIMEOUT_SECONDS, metadata=metadata)

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


def run():
    identify_emotion()


if __name__ == '__main__':
    run()
