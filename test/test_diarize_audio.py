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
from deepaffects.models.diarize_audio import DiarizeAudio


class TestDiarizeAudio(unittest.TestCase):
    """ DiarizeAudio unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDiarizeAudio(self):
        """
        Test DiarizeAudio
        """
        model = deepaffects.models.diarize_audio.DiarizeAudio()


if __name__ == '__main__':
    unittest.main()
