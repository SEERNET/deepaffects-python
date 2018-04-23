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
from deepaffects import Audio
from deepaffects.rest import ApiException
from deepaffects.apis.diarize_api_v2 import DiarizeApiV2
from .test_base_setup import DIR
import uuid


class TestDiarizeApiV2(unittest.TestCase):
    """ DiarizeApiV2 unit test stubs """

    def setUp(self):
        deepaffects.configuration.api_key['apikey'] = os.environ['DEEPAFFECTS_API_KEY']
        self.webhook_url = os.environ["DEEPAFFECTS_API_WEBHOOK"]
        self.api = deepaffects.apis.diarize_api_v2.DiarizeApiV2()
        self.request_id = str(uuid.uuid4())

    def tearDown(self):
        pass

    def test_async_diarize_audio(self):
        """
        Test case for diarize_audio

        Diarize an audio file
        """
        test_conversation_audio = os.path.normpath(os.path.join(DIR, "data/happy.mp3"))
        body = Audio.from_file(file_name=test_conversation_audio)

        api_response = self.api.async_diarize_audio(body=body, webhook=self.webhook_url, request_id=self.request_id)
        self.assertTrue(api_response.request_id, self.request_id)

if __name__ == '__main__':
    unittest.main()
