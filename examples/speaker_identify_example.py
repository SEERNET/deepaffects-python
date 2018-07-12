from deepaffects.realtime.util import get_segment_chunk_from_pydub_chunk, get_deepaffects_client, chunk_generator_from_file

TIMEOUT_SECONDS = 300
API_KEY = "YOUR_API_KEY"
file_path = "FILE_PATH"
languageCode = "en-Us"
sampleRate = 16000
encoding = "wav"
userIds = "list of userids for for speaker verification"

# DeepAffects realtime Api client
client = get_deepaffects_client()

# chunk_generator() is a generator function which yields audio segment object asynchronously
metadata = [
    ('apikey', apikey),
    ('userids', userIds),
    ('encoding', encoding),
    ('samplerate', sampleRate),
    ('languagaecode', languageCode)
]

responses = client.IdentifySpeaker(
    chunk_generator_from_file(file_path), TIMEOUT_SECONDS, metadata=metadata)

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
