from deepaffects.realtime.util import get_deepaffects_client, chunk_generator_from_file, chunk_generator_from_url

TIMEOUT_SECONDS = 3000
apikey = "Pnpr9E0nEWEdVByJoGxquE7EPjbFLB0W"
file_path = "/Users/VivekNimkarde/DeepAffects/my_files/TSLA-q1-2018.mp3"
languageCode = "en-Us"
sampleRate = "16000"
encoding = "mp3"
userIds = "ElonMusk"
# DeepAffects realtime Api client
client = get_deepaffects_client()

# chunk_generator() is a generator function which yields audio segment object asynchronously
metadata = [
    ('apikey', apikey),
    ('userids', userIds),
    ('encoding', encoding),
    ('samplerate', sampleRate),
    ('languagecode', languageCode)
]

"""Stream audio from url or youtube.

responses = client.IdentifySpeaker(
    chunk_generator_from_url(file_path, is_youtube_url=is_youtube_url), TIMEOUT_SECONDS, metadata=metadata)
"""

"""Stream audio from local file.
"""
generator = chunk_generator_from_file(file_path)

responsesSpeaker = client.IdentifySpeaker(
    generator, TIMEOUT_SECONDS, metadata=metadata)
responsesEmotion = client.IdentifyEmotion(
    generator, TIMEOUT_SECONDS, metadata=metadata)

# responses is the iterator for all the response values
for response in responsesSpeaker:
    print("Received message")
    print(response)


# responses is the iterator for all the response values
for response in responsesEmotion:
    print("Received message")
    print(response)

# responses = client.IdentifyEmotion(
#     chunk_generator_from_file(file_path), TIMEOUT_SECONDS, metadata=metadata)

# # responses is the iterator for all the response values
# for response in responses:
#     print("Received message")
#     print(response)

"""Response.

    response = {           
        speaker: speaker identified in the segment,
        start: start of the segment,
        end: end of the segment
    }
"""
