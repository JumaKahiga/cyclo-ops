"""
Base classes to be subclassed by TestCases
"""
import unittest

import cyclops.app


class EndpointTestCase(unittest.TestCase):
    def setUp(self):
        """Create test app and client."""

        self.app = cyclops.app.create_app(TESTING=True)
        self.app_client = self.app.test_client()
