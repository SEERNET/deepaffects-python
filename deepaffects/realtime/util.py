from __future__ import print_function

import random
import time
import grpc
import os
import io
import sys
import pydub
import base64
from pydub import AudioSegment
from pytube.request import get
from pytube import YouTube

import deepaffects.realtime.deepaffects_realtime_pb2_grpc as deepaffects_grpc
import deepaffects.realtime.deepaffects_realtime_pb2 as deepaffects_types
from deepaffects.realtime.types import segment_chunk


def encode_to_base64(file):
    with open(file, "rb") as f1:
        return base64.b64encode(f1.read()).decode('utf-8')


def get_segment_chunk_from_pydub_chunk(chunk, offset, i, userIds=None):

    base64_chunk = pydub_segment_to_base64(chunk)
    print("Sending chunk %s - with size :- %s sec" % (i, len(chunk) / 1000))
    audio_segments = segment_chunk(
        encoding="wav",
        languageCode="en-US",
        sampleRate=8000,
        content=base64_chunk,
        duration=len(chunk) / 1000,
        userIds=userIds,
        segmentOffset=offset)
    offset = (offset + len(chunk) / 1000)
    return audio_segments, offset


def pydub_segment_to_base64(chunk):
    chunk_file = "chunk.wav"
    with open(chunk_file, "wb") as f:
        chunk.export(f, format="wav")
    base64_chunk = encode_to_base64(chunk_file)
    os.remove(chunk_file)
    return base64_chunk


def get_deepaffects_client(host_url='realtime.deepaffects.com:80'):
    channel = grpc.insecure_channel(host_url)
    stub = deepaffects_grpc.DeepAffectsRealtimeStub(channel)
    return stub


def chunk_generator_from_file(file_path, max_chunk_size=15500, min_chunk_size=3000):
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


def chunk_generator_from_url(file_path, is_youtube_url=False, chunk_size=15 * 8192):
    if is_youtube_url:
        yt = YouTube(file_path)
        stream = yt.streams.filter(only_audio=True).first()
        download_url = stream.url
    else:
        download_url = file_path

    final_chunk = None
    last_seg_len = 0
    for i, chunk in enumerate(get(url=download_url, streaming=True, chunk_size=chunk_size)):
        if final_chunk is None:
            final_chunk = chunk
        else:
            final_chunk = final_chunk + chunk
        seg = AudioSegment.from_file(io.BytesIO(
            final_chunk))
        audio_segment, offset = get_segment_chunk_from_pydub_chunk(
            seg[last_seg_len:], last_seg_len / 1000, i)
        yield audio_segment
        last_seg_len = int(seg.duration_seconds * 1000)
