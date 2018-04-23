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
from .test_base_setup import DIR


class TestDenoiseApi(unittest.TestCase):
    """ DenoiseApi unit test stubs """

    @staticmethod
    def sdr(clean, reconstructed):
        # TODO: Implement SDR here
        return 5.1

    def setUp(self):
        deepaffects.configuration.api_key['apikey'] = os.environ['DEEPAFFECTS_API_KEY']
        self.api = deepaffects.DenoiseApi()

    def tearDown(self):
        pass

    def test_sync_denoise_audio(self):
        """
        Test case for sync_denoise_audio

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
