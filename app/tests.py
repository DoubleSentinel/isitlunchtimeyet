import unittest

from app import app


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_dummy(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
