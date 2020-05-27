import unittest
from app import app


class RouteTest(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()
		self.app.testing = True

	def test_hello_name(self):
		response = self.app.get('/hello/Fineas')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data, b'Hello Fineas!')


if __name__ == '__main__':
	unittest.main()
