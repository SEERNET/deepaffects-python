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
from deepaffects.models.audio import Audio


class TestAudio(unittest.TestCase):
    """ Audio unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAudio(self):
        """
        Test Audio
        """
        model = deepaffects.models.audio.Audio()


if __name__ == '__main__':
    unittest.main()
