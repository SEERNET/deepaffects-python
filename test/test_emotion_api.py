# coding: utf-8

"""
    DeepAffects

    OpenAPI Specification of DeepAffects APIs

    OpenAPI spec version: v1
"""

from __future__ import absolute_import

import os
import sys
import unittest

from deepaffects import Audio
import uuid
import deepaffects
from deepaffects.rest import ApiException
from deepaffects.apis.emotion_api import EmotionApi
from deepaffects.models.emotion_score import EmotionScore
from .test_base_setup import DIR



class TestEmotionApi(unittest.TestCase):
    """ EmotionApi unit test stubs """

    def setUp(self):
        deepaffects.configuration.api_key['apikey'] = os.environ['DEEPAFFECTS_API_KEY']
        self.webhook_url = os.environ["DEEPAFFECTS_API_WEBHOOK"]                
        self.api = deepaffects.apis.emotion_api.EmotionApi()

    def tearDown(self):
        pass

    def test_async_recognise_emotion_with_request_id(self):
        """
        Test case for async_recognise_emotion

        Find emotion in an audio file
        """
        self.request_id = str(uuid.uuid4())
        test_happy_audio = os.path.normpath(os.path.join(DIR, "data/happy.mp3"))
        body = Audio.from_file(file_name=test_happy_audio)        
        api_response = self.api.async_recognise_emotion(body=body, webhook=self.webhook_url, request_id=self.request_id)
        print(api_response)
        assert api_response.request_id, self.request_id
    def test_async_recognise_emotion_without_request_id(self):
        """
        Test case for async_recognise_emotion

        Find emotion in an audio file
        """
        test_happy_audio = os.path.normpath(os.path.join(DIR, "data/happy.mp3"))
        body = Audio.from_file(file_name=test_happy_audio)        
        api_response = self.api.async_recognise_emotion(body=body, webhook=self.webhook_url)
        print(api_response)
        assert api_response.request_id

    def test_sync_recognise_emotion(self):
        """
        Test case for sync_recognise_emotion

        Find emotion in an audio file
        """
        test_happy_audio = os.path.normpath(os.path.join(DIR, "data/happy.mp3"))
        body = Audio.from_file(file_name=test_happy_audio)
        api_response = self.api.sync_recognise_emotion(body=body)
        print(api_response)
        for obj in api_response:
            if obj.emotion == 'Happy':
                assert obj.score > 0.8


if __name__ == '__main__':
    unittest.main()
