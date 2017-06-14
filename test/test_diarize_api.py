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
from deepaffects.rest import ApiException
from deepaffects.apis.diarize_api import DiarizeApi


class TestDiarizeApi(unittest.TestCase):
    """ DiarizeApi unit test stubs """

    def setUp(self):
        self.api = deepaffects.apis.diarize_api.DiarizeApi()

    def tearDown(self):
        pass

    def test_async_diarize_audio(self):
        """
        Test case for diarize_audio

        Diarize an audio file
        """
        pass


if __name__ == '__main__':
    unittest.main()
