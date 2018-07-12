# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the gRPC route guide client."""

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


def get_deepaffects_client():
    channel = grpc.insecure_channel('localhost:50051')
    stub = deepaffects_grpc.DeepAffectsRealtimeStub(channel)
    return stub


def chunk_generator_from_file(file_path, min_chunk_size=3000, max_chunk_size=15500):
    # Implement this generator function to yield Audio segments
    # To generate Audio Segments use make_input_audio_segment
    """chunk_generator_from_file.

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

    for i, chunk in enumerate(audio_clip[::15500]):

        if offset is None:
            offset = 0

        if previous_chunk is not None:

            if len(chunk) <= 3000:

                previous_chunk = previous_chunk + chunk
                audio_segment, offset = get_segment(previous_chunk, offset, i)
                yield audio_segment

            elif (len(chunk) < 15500) and (len(chunk) > 3000):

                audio_segment, offset = get_segment(previous_chunk, offset, i)
                previous_chunk = chunk
                yield audio_segment
                audio_segment, offset = get_segment(previous_chunk, offset, i)
                yield audio_segment

            else:

                audio_segment, offset = get_segment(previous_chunk, offset, i)
                previous_chunk = chunk
                yield audio_segment

        if previous_chunk is None:
            previous_chunk = chunk


# def generate_chunks():
#     # split sound in 5-second slices and export
#     audio_clip = AudioSegment.from_file("modi_video.mp4")
#     for i, chunk in enumerate(audio_clip[::1000]):
#         time.sleep(1)
#         chunk_name = "chunk.wav"
#         with open(chunk_name, "wb") as f:
#             chunk.export(f, format="wav")
#         base64_chunk = encode_to_base64(chunk_name)
#         os.remove(chunk_name)
#         print("Sending chunk %s" % (i))
#         yield make_input_audio_segment(i, base64_chunk)


# def identify_speaker(stub):
#     responses = stub.GetSpeaker(generate_chunks())
#     for response in responses:
#         print("Received message %s at %s" % (response.id,
#                                              response.speaker))


# def run():
#     channel = grpc.insecure_channel('localhost:50051')
#     stub = audio_stream_pb2_grpc.DeepAffectsApiStub(channel)
#     print("-------------- Realtime Api --------------")
#     get_speaker(stub)


# if __name__ == '__main__':
#     run()
