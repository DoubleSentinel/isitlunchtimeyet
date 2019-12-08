import unittest

from app import app as FLASK_APP


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = FLASK_APP.test_client()

    def test_dummy(self):
        response = self.app.get("/api")
        self.assertEqual(response.status_code, 200)
        self.assertEqual('to implement', response.data.decode('utf-8'))

    def test_simple_api(self):
        response = self.app.get('/api/lunch')
        # request returns 200, but fails because we cannot use the ip-api
        # because the test uses 127.0.0.1 and is not valid
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn('status', data)
        self.assertIn('errorMessage', data)
        self.assertNotIn('lunchtime', data)
        self.assertNotIn('flavorMessage', data)
        self.assertEqual('error', data['status'])


if __name__ == '__main__':
    unittest.main()
