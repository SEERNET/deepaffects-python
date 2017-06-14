# coding: utf-8

"""
    DeepAffects

    OpenAPI spec version: v1
"""


from __future__ import absolute_import

import os
import sys
import unittest

import deepaffects
from deepaffects.models.audio import Audio
from .test_base_setup import DIR, AudioTest


class TestDenoiseApi(unittest.TestCase):
    """ DenoiseApi unit test stubs """

    def initialize_api(self):
        self.api = deepaffects.DenoiseApi()

    def tearDown(self):
        pass

    def test_async_denoise_audio(self):
        """
        Test case for async_denoise_audio

        Denoise an audio file
        """
        test_noisy_audio = os.path.normpath(os.path.join(DIR, "data/noisy.wav"))
        test_clean_audio = os.path.normpath(os.path.join(DIR, "data/clean.wav"))
        test_reconstructed_audio = os.path.normpath(os.path.join(DIR, "data/reconstructed.wav"))
        body = Audio.from_file(file_name=test_noisy_audio)
        api_response = self.api.sync_denoise_audio(body=body)
        api_response.to_file(test_reconstructed_audio)
        self.assertTrue(TestDenoiseApi.sdr(test_clean_audio, test_reconstructed_audio) > 5)
        pass


if __name__ == '__main__':
    unittest.main()
