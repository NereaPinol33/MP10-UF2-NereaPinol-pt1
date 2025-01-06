import unittest
from gestio_erp.orders import Order
from gestio_erp.products import Product
from gestio_erp.exceptions import ProductNotFoundException

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.order = Order(101)
        self.product = Product("bicicleta")

    def test_order_creation(self):
        self.assertEqual(self.order.order_id, 101)
        self.assertEqual(self.order.status, Order.PENDING)

    def test_add_product(self):
        self.order.add_product(self.product)
        self.assertIn(self.product, self.order.products)
        self.assertEqual(self.order.products[self.product], 1)

    def test_add_product_with_quantity(self):
        self.order.add_product(self.product, 3)
        self.assertEqual(self.order.products[self.product], 3)

    def test_increase_quantity(self):
        self.order.add_product(self.product, 2)
        self.order.increase_quantity(self.product, 3)
        self.assertEqual(self.order.products[self.product], 5)

    def test_remove_product(self):
        self.order.add_product(self.product, 3)
        self.order.remove_product(self.product, 2)
        self.assertEqual(self.order.products[self.product], 1)

    def test_remove_product_entirely(self):
        self.order.add_product(self.product, 2)
        self.order.remove_product(self.product)
        self.assertNotIn(self.product, self.order.products)

    def test_modify_status(self):
        self.order.modify_status(Order.SENT)
        self.assertEqual(self.order.status, Order.SENT)

    def test_summary(self):
        self.order.add_product(self.product, 2)
        summary = self.order.summary()
        self.assertIn("bicicleta: 2", summary)

if __name__ == "__main__":
    unittest.main()
