import unittest

from pyramid import testing
from backend.backend import add_endpoints


class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        add_endpoints(self.config)


    def tearDown(self):
        testing.tearDown()

    def test_hello_world(self):
        from backend.backend import hello_world_endpoint
        request = testing.DummyRequest()
        response = hello_world_endpoint(request)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.body,b"Hello World!")