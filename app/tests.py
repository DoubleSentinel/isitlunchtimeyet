import unittest

from app import app as FLASK_APP


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = FLASK_APP.test_client()

    def test_dummy(self):
        response = self.app.get("/api")
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual('to implement', response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
