from deepaffects.realtime.util import get_deepaffects_client, chunk_generator_from_url

TIMEOUT_SECONDS = 2000
apikey = "API_KEY"
file_url = "FILE_PATH"
is_youtube = False
languageCode = "en-Us"
sampleRate = "16000"
encoding = "wav"
userIds = "list of userids for for speaker verification seperated by ','"

# DeepAffects realtime Api client
client = get_deepaffects_client()

metadata = [
    ('apikey', apikey),
    ('userids', userIds),
    ('encoding', encoding),
    ('samplerate', sampleRate),
    ('languagaecode', languageCode)
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

responses = client.IdentifyEmotion(
    chunk_generator_from_url(file_url, is_youtube=is_youtube), TIMEOUT_SECONDS, metadata=metadata)

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
