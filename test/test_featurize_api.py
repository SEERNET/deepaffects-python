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
from deepaffects.apis.featurize_api import FeaturizeApi


class TestFeaturizeApi(unittest.TestCase):
    """ FeaturizeApi unit test stubs """

    def setUp(self):
        self.api = deepaffects.apis.featurize_api.FeaturizeApi()

    def tearDown(self):
        pass

    def test_async_featurize_audio(self):
        """
        Test case for featurize_audio

        featurize an audio file
        """
        pass


if __name__ == '__main__':
    unittest.main()
