import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_ask_endpoint(self):
        response = self.app.post('/ask', json={'question': 'What is 2+2?'})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
