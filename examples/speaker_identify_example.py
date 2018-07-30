from deepaffects.realtime.util import get_deepaffects_client, chunk_generator_from_file, chunk_generator_from_url

TIMEOUT_SECONDS = 10000
apikey = "YOUR_API_KEY"
file_path = "FILE_PATH"
is_youtube_url = False
languageCode = "en-Us"
sampleRate = "16000"
encoding = "wav"
apiVersion = "v2"
userIds = "list of userids for for speaker verification seperated by ','"

# DeepAffects realtime Api client
client = get_deepaffects_client()

# chunk_generator() is a generator function which yields audio segment object asynchronously
metadata = [
    ('apikey', apikey),
    ('userids', userIds),
    ('encoding', encoding),
    ('samplerate', sampleRate),
    ('languagecode', languageCode),
    ('apiversion', apiVersion)
]

"""Stream audio from url or youtube.

responses = client.IdentifySpeaker(
    chunk_generator_from_url(file_path, is_youtube_url=is_youtube_url), TIMEOUT_SECONDS, metadata=metadata)
"""

"""Stream audio from local file.
"""
responses = client.IdentifySpeaker(
    chunk_generator_from_file(file_path max_chunk_size=30000), TIMEOUT_SECONDS, metadata=metadata)

# responses is the iterator for all the response values
for response in responses:
    print("Received message")
    print(response)

"""Response.

    response = {           
        userId: userId of the speaker identified in the segment,
        start: start of the segment,
        end: end of the segment
    }
"""
