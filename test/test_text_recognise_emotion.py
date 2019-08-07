# coding: utf-8

"""
    DeepAffects

    OpenAPI spec version: v1
"""


from __future__ import absolute_import

import os
import sys
import unittest

sys.path.insert(0, '/Users/VivekNimkarde/DeepAffects/deepaffects-python')
import deepaffects
from deepaffects import Audio
from deepaffects.rest import ApiException
from .test_base_setup import DIR
import uuid


class TestTextEmootion(unittest.TestCase):
    """ Text Emotion unit test stubs """

    def setUp(self):
        deepaffects.configuration.api_key['apikey'] = os.environ['DEEPAFFECTS_API_KEY']        
        self.api = deepaffects.apis.emotion_api.EmotionApi()

    def tearDown(self):
        pass

    def test_sync_diarize_audio_sample_text(self):
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
    def test_sync_diarize_audio_check_response_field_exists(self):
        """
        Test case for Text Emotion

        Diarize text file
        """

        body = {
            "content": "Awesome"
        }
        api_response = self.api.sync_text_recognise_emotion(body=body)        
        print(api_response)
        assert api_response['response']
    def test_sync_diarize_audio_check_version_field_exists(self):
        """
        Test case for Text Emotion

        Diarize text file
        """

        body = {
            "content": "Awesome"
        }
        api_response = self.api.sync_text_recognise_emotion(body=body)        
        print(api_response)
        assert api_response['version']


if __name__ == '__main__':
    unittest.main()
