import sys
from pydub import AudioSegment
from random import randint
import time
from deepaffects.realtime.util import get_segment_chunk_from_pydub_chunk, get_deepaffects_client


TIMEOUT_SECONDS = 2000
API_KEY = "YOUR_API_KEY"
file_path = "FILE_PATH"


def chunk_generator_from_file(file_path, max_chunk_size=15500, min_chunk_size=3000):
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

    for i, chunk in enumerate(audio_clip[::max_chunk_size]):

        if offset is None:
            offset = 0

        if previous_chunk is not None:

            if len(chunk) <= min_chunk_size:

                previous_chunk = previous_chunk + chunk
                audio_segment, offset = get_segment_chunk_from_pydub_chunk(
                    previous_chunk, offset, i)
                yield audio_segment

            elif (len(chunk) < max_chunk_size) and (len(chunk) > min_chunk_size):

                audio_segment, offset = get_segment_chunk_from_pydub_chunk(
                    previous_chunk, offset, i)
                previous_chunk = chunk
                yield audio_segment
                audio_segment, offset = get_segment_chunk_from_pydub_chunk(
                    previous_chunk, offset, i)
                yield audio_segment

            else:

                audio_segment, offset = get_segment_chunk_from_pydub_chunk(
                    previous_chunk, offset, i)
                previous_chunk = chunk
                yield audio_segment

        if previous_chunk is None:
            if len(audio_clip) < max_chunk_size:
                audio_segment, offset = get_segment_chunk_from_pydub_chunk(
                    chunk, offset, i)
                yield audio_segment
            previous_chunk = chunk


def identify_emotion():

    # DeepAffects realtime Api client
    client = get_deepaffects_client()

    metadata = [('apikey', API_KEY)]
    # chunk_generator() is a generator function which yields audio segment object asynchronously
    responses = client.IdentifyEmotion(
        chunk_generator_from_file(FILE_PATH), TIMEOUT_SECONDS, metadata=metadata)

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
