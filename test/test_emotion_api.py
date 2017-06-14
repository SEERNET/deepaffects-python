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

import deepaffects
from deepaffects.rest import ApiException
from deepaffects.apis.emotion_api import EmotionApi


class TestEmotionApi(unittest.TestCase):
    """ EmotionApi unit test stubs """

    def setUp(self):
        self.api = deepaffects.apis.emotion_api.EmotionApi()

    def tearDown(self):
        pass

    def test_async_recognise_emotion(self):
        """
        Test case for async_recognise_emotion

        Find emotion in an audio file
        """
        pass

    def test_sync_recognise_emotion(self):
        """
        Test case for sync_recognise_emotion

        Find emotion in an audio file
        """
        pass


if __name__ == '__main__':
    unittest.main()
