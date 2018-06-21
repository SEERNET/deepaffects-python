# coding: utf-8

"""
    DeepAffects

    OpenAPI spec version: v1
"""


from __future__ import absolute_import

import os
import sys
import unittest
import uuid
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
        self.webhook_url = os.environ["DEEPAFFECTS_API_WEBHOOK"]

    def tearDown(self):
        pass
    def test_async_denoise_audio(self):
        """
        Test case for sync_denoise_audio

        Denoise an audio file 
        """
        self.request_id = str(uuid.uuid4())
        test_noisy_audio = os.path.normpath(os.path.join(DIR, "data/noisy.wav"))
        body = Audio.from_file(file_name=test_noisy_audio)
        api_response = self.api.async_denoise_audio(body=body, webhook=self.webhook_url, request_id=self.request_id)
        assert api_response.request_id, self.request_id

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
        assert TestDenoiseApi.sdr(test_clean_audio, test_reconstructed_audio) > 5        


if __name__ == '__main__':
    unittest.main()
