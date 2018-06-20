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
DIR = os.path.dirname(os.path.realpath(__file__))
import uuid


class TestTextEmootion(unittest.TestCase):
    """ Text Emotion unit test stubs """

    def setUp(self):
        deepaffects.configuration.api_key['apikey'] = os.environ['DEEPAFFECTS_API_KEY']
        self.webhook_url = os.environ["DEEPAFFECTS_API_WEBHOOK"]
        self.api = deepaffects.apis.emotion_api.EmotionApi()
        self.request_id = str(uuid.uuid4())

    def tearDown(self):
        pass

    def test_async_diarize_audio(self):
        """
        Test case for Text Emotion

        Diarize text file
        """

        body = {
            "content": "Awesome"
        }
        api_response = self.api.sync_text_recognise_emotion(body=body)        
        print(api_response)
        assert api_response['response']['trust']> 0.8


if __name__ == '__main__':
    unittest.main()
