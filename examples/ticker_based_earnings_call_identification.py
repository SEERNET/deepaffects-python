from deepaffects.realtime.util import get_deepaffects_client, chunk_generator_from_file, chunk_generator_from_url, chunk_generator_from_playlist

TIMEOUT_SECONDS = 10000
apikey = "YOUR_API_KEY"
file_path = "PLAYLIST_PATH"
ticker = "TICKER_SYMBOL"
out_file_name = "OUT_FILE_NAME"
languageCode = "en-Us"
verbose = "True"

metadata = [
    ('apikey', apikey),        
    ('languagecode', languageCode),    
    ('ticker', ticker),
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
# DeepAffects realtime Api client
client = get_deepaffects_client()

responses = client.DiarizeEmotion(
    chunk_generator_from_playlist(out_file_name=out_file_name, file_path=file_path), TIMEOUT_SECONDS, metadata=metadata)

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
