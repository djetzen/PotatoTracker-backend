import unittest

from pyramid import testing


class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_hello_world(self):
        from backend.backend import add_hello_world_endpoint

        request = testing.DummyRequest()
        response = add_hello_world_endpoint(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.body,b"Hello World!")