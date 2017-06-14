# coding: utf-8

"""
    DeepAffects

    OpenAPI Specification of DeepAffects APIs

    OpenAPI spec version: 0.1.0
"""


from __future__ import absolute_import

import os
import sys
import unittest

import deepaffects
from deepaffects.rest import ApiException
from deepaffects.models.async_response import AsyncResponse


class TestAsyncResponse(unittest.TestCase):
    """ AsyncResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAsyncResponse(self):
        """
        Test AsyncResponse
        """
        model = deepaffects.models.async_response.AsyncResponse()


if __name__ == '__main__':
    unittest.main()
