from unittest import TestCase
from fastapi.testclient import TestClient
from main import app


class TestCart(TestCase):
    client = TestClient(app)

    def test_add_to_cart(self):
        product = {
            "name": "Laptop",
            "brand": "HP Z100",
            "price": 1000
        }

        expected_response = {
            "status_code": 201,
            "message": "Created product"
        }

        response = self.client.post(
            url="/cart",
            json=product
        )

        self.assertEqual(
            response.status_code, expected_response["status_code"]
        )

        self.assertEqual(
            response.json()["message"], expected_response["message"]
        )

        expected_response = 200

        response = self.client.delete(
            url="/cart/{1}",
        )

        self.assertEqual(
            response.status_code, expected_response
        )