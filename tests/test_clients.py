import unittest
from gestio_erp.clients import Client
from gestio_erp.orders import Order

class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client(1, "Anna", "anna@example.com")
        self.order = Order(101)

    def test_client_creation(self):
        self.assertEqual(self.client.client_id, 1)
        self.assertEqual(self.client.name, "Anna")
        self.assertEqual(self.client.email, "anna@example.com")

    def test_add_order(self):
        self.client.add_order(self.order)
        self.assertIn(self.order, self.client.list_orders())

    def test_list_orders_empty(self):
        self.assertEqual(len(self.client.list_orders()), 0)

    def test_list_orders_with_orders(self):
        self.client.add_order(self.order)
        self.assertEqual(len(self.client.list_orders()), 1)

    def test_str_representation(self):
        self.assertEqual(str(self.client), "Client(1, Anna, anna@example.com)")

if __name__ == "__main__":
    unittest.main()
