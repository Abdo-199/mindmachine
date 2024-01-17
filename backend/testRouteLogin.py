import unittest
from fastapi.testclient import TestClient
from api import API
from dataDefinitions import LoginRequestModel




class APITestCase(unittest.TestCase):

    def setUp(self):
        self.api_instance = API()

        self.client = TestClient(self.api_instance.app)

    def test_validate_credentials_success(self):
        request_data = {"username": "s0561626", "password": "Titicamara7!"}

        response = self.client.post("/api/login", json=request_data)

        self.assertEqual(response.status_code, 200)
        result = response.json()

        self.assertTrue(result["isAuthenticated"])
        self.assertFalse(result["isAdmin"])



if __name__ == '__main__':
    unittest.main()
