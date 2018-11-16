from __future__ import print_function

import random
import time
import grpc
import os
import io
import sys
import pydub
import base64
import uuid
from pydub import AudioSegment
from pytube.request import get
from pytube import YouTube

import deepaffects.realtime.deepaffects_realtime_pb2_grpc as deepaffects_grpc
import deepaffects.realtime.deepaffects_realtime_pb2 as deepaffects_types
from deepaffects.realtime.types import segment_chunk


def encode_to_base64(file):
    with open(file, "rb") as f1:
        return base64.b64encode(f1.read()).decode('utf-8')


def get_segment_chunk_from_pydub_chunk(chunk, offset, i):
    base64_chunk = pydub_segment_to_base64(chunk,i)
    print("Sending chunk %s - with size :- %s sec" % (i, len(chunk) / 1000))
    audio_segments = segment_chunk(
        encoding="wav",
        languageCode="en-US",
        sampleRate=chunk.frame_rate,
        content=base64_chunk,
        duration=len(chunk) / 1000,        
        segmentOffset=offset)
    offset = (offset + len(chunk) / 1000)
    return audio_segments, offset


def pydub_segment_to_base64(chunk,i):    
    chunk_file = "chunk-{}-{}.wav".format(i, str(uuid.uuid4()))
    chunk.export(chunk_file, format="wav")        
    base64_chunk = encode_to_base64(chunk_file)
    try:
        os.remove(chunk_file)
    except:
        pass    
    return base64_chunk


def get_deepaffects_client(host_url='realtime.deepaffects.com:80'):
    channel = grpc.insecure_channel(host_url)
    stub = deepaffects_grpc.DeepAffectsRealtimeStub(channel)
    return stub


def chunk_generator_from_file(file_path, buffer_size=30000):
    # Implement this generator function to yield Audio segments
    # To generate Audio Segments use segment_chunk
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
    audio_clip = AudioSegment.from_file(file_path)
    offset = None
    buffer_chunk = None
    index = 0
    for i, chunk in enumerate(audio_clip[::buffer_size]):
        if offset is None:
            offset = 0
        if i == 0:
            buffer_chunk = chunk
        else:
            buffer_chunk = buffer_chunk + chunk
        offset_in_milliseconds = offset * 1000        
        if ((len(buffer_chunk) - (offset_in_milliseconds)) > buffer_size):            
            segment_chunk = buffer_chunk[offset_in_milliseconds: offset_in_milliseconds + buffer_size]            
            audio_segment, offset = get_segment_chunk_from_pydub_chunk(segment_chunk, offset, index)
            index = index + 1
            yield audio_segment        

    if ((len(buffer_chunk) - (offset * 1000)) != 0):        
        segment_chunk = buffer_chunk[offset * 1000:]
        audio_segment, offset = get_segment_chunk_from_pydub_chunk(segment_chunk, offset, index)
        index = index + 1
        yield audio_segment
        


def chunk_generator_from_url(file_path, is_youtube_url=False, buffer_size=30000, chunk_size=15 * 8192):
    if is_youtube_url:
        yt = YouTube(file_path)
        stream = yt.streams.filter(only_audio=True).first()
        download_url = stream.url
    else:
        download_url = file_path
    offset = None
    buffer_chunk = None
    index = 0
    for i, chunk in enumerate(get(url=download_url, streaming=True, chunk_size=chunk_size)):        
        if offset is None:
            offset = 0
        if i == 0:
            buffer_chunk_raw = chunk
        else:
            buffer_chunk_raw = buffer_chunk_raw + chunk

        buffer_chunk = AudioSegment.from_file(io.BytesIO(
            buffer_chunk_raw))

        offset_in_milliseconds = offset * 1000
        if (len(buffer_chunk) - (offset_in_milliseconds)) > buffer_size:            
            segment_chunk = buffer_chunk[offset_in_milliseconds: offset_in_milliseconds + buffer_size]            
            audio_segment, offset = get_segment_chunk_from_pydub_chunk(segment_chunk, offset, index)
            index = index + 1
            yield audio_segment        
    if (len(buffer_chunk) - (offset * 1000)) != 0:        
        segment_chunk = buffer_chunk[offset * 1000:]
        audio_segment, offset = get_segment_chunk_from_pydub_chunk(segment_chunk, offset, index)
        index = index + 1
        yield audio_segment
