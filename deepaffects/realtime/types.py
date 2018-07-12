from deepaffects.realtime.deepaffects_realtime_pb2 import SegmentChunk


def segment_chunk(content, encoding="wav", languageCode="en-US", sampleRate=8000, segmentOffset=0, duration=0, userIds=None):
    """segment_chunk.

    Args:
        encoding : Audio Encoding,
        languageCode: language code , 
        sampleRate: sample rate of audio , 
        content: base64 encoded audio, 
        duration: in seconds,
        segmentOffset: offset of the segment in complete audio stream
    """

    if duration < 3:
        raise ValueError('Chunk duration should be greater than 3 sec.')

    return SegmentChunk(
        content=content,
        encoding=encoding,
        languageCode=languageCode,
        sampleRate=sampleRate,
        userIds=userIds,
        duration=duration,
        segmentOffset=segmentOffset)
