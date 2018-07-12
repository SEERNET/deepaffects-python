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


configuration = {
    "TIMEOUT_SECONDS" = 2000,
    "API_KEY" = ""
}


def get_deepaffects_client():
    channel = grpc.insecure_channel('realtime.deepaffects.com:80')
    stub = deepaffects_grpc.DeepAffectsRealtimeStub(channel)
    return stub


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
