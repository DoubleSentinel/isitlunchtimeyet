import unittest

from app import app as FLASK_APP


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = FLASK_APP.test_client()

    def json_format(self, response):
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn('status', data)
        self.assertNotIn('errorMessage', data)
        self.assertIn('time', data)
        self.assertIn('flavorMessage', data)
        self.assertEqual('ok', data['status'])

    #    def test_simple_lunch(self):
    #        response = self.app.get('/api/lunch')
    #        # request returns 200, but fails because we cannot use the ip-api
    #        # because the test uses 127.0.0.1 and is not valid
    #        self.json_format(response)

    def test_req_api_lunch_time(self):
        response = self.app.get('/api/lunch/12/45')

        self.json_format(response)


if __name__ == '__main__':
    unittest.main()
