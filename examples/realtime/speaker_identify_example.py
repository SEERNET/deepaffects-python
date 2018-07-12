from pydub import AudioSegment
from random import randint
import time
from deepaffects.realtime.util import get_segment_chunk_from_pydub_chunk, get_deepaffects_client

TIMEOUT_SECONDS = 300
API_KEY = "h4CVE1DPwxRIVRGZYRmfVUpcObDcr5tr"
file_path = "/Users/VivekNimkarde/Deepaffects/my_files/p225_006.wav"
userIds = "p225"


def chunk_generator():
    # Implement this generator function to yield Audio segments
    # to generate Audio Segments
    """segment_chunk.

    Args:
        encoding : Audio Encoding,
        languageCode: language code , 
        sampleRate: sample rate of audio , 
        content: base64 encoded audio, 
        offset: offset of the segment in complete audio stream,
        duration: audio duration
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
                audio_segment, offset = get_segment_chunk_from_pydub_chunk(
                    previous_chunk, offset, i)
                yield audio_segment

            elif (len(chunk) < 15500) and (len(chunk) > 3000):

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
            if len(audio_clip) < 15500:
                audio_segment, offset = get_segment_chunk_from_pydub_chunk(
                    chunk, offset, i)
                yield audio_segment
            previous_chunk = chunk


def identify_emotion():

    # DeepAffects realtime Api client
    client = get_deepaffects_client()

    # chunk_generator() is a generator function which yields audio segment object asynchronously
    metadata = [('apikey', API_KEY), ('userids', userIds)]

    responses = client.IdentifySpeaker(
        chunk_generator(), TIMEOUT_SECONDS, metadata=metadata)

    # responses is the iterator for all the response values
    for response in responses:
        print("Received message")
        print(response)

    """Response.

       response = {           
           speaker: speaker identified in the segment,
           start: start of the segment,
           end: end of the segment
       }
    """


def run():
    identify_emotion()


if __name__ == '__main__':
    run()
