from deepaffects.realtime.util import get_deepaffects_client, chunk_generator_from_file, chunk_generator_from_url

TIMEOUT_SECONDS = 10000
apikey = "YOUR_API_KEY"
file_path = "FILE_PATH"
is_youtube_url = False
languageCode = "en-Us"
sampleRate = "16000"
encoding = "wav"
speakerIds = "list of userids for for speaker verification seperated by ','"
verbose = "True"
# DeepAffects realtime Api client
client = get_deepaffects_client()

metadata = [
    ('apikey', apikey),
    ('encoding', encoding),
    ('speakerids', speakerIds),
    ('samplerate', sampleRate),
    ('languagecode', languageCode),
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

"""Stream audio from url or youtube.

responses = client.DiarizeEmotion(
    chunk_generator_from_url(file_path, is_youtube_url=is_youtube_url), TIMEOUT_SECONDS, metadata=metadata)
"""

"""Stream audio from local file.
"""
responses = client.DiarizeEmotion(
    chunk_generator_from_file(file_path), TIMEOUT_SECONDS, metadata=metadata)


# responses is the iterator for all the response values
for response in responses:
    print("Received message")
    print(response)

"""Response.
    response = {
        userId: userId of the speaker identified in the segment,
        emotion: Emotion identified in the segment,
        start: start of the segment,
        end: end of the segment
    }
"""
