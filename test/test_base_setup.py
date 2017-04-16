import os
from unittest import TestCase, SkipTest

import deepaffects

DIR = os.path.dirname(os.path.realpath(__file__))

class AudioTest(TestCase):
    def initialize_api(self):
        pass

    def setUp(self):
        self.api_key = os.getenv("DEEPAFFECTS_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API Key needs to be defined in an environment variable DEEPAFFECTS_API_KEY to run tests."
            )
        deepaffects.configuration.api_key = self.api_key
        self.initialize_api()

    @staticmethod
    def _require_numpy():
        try:
            import numpy as np
            return np
        except ImportError:
            raise SkipTest("Numpy is not installed!")

