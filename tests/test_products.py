import unittest
from gestio_erp.products import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product("bicicleta")

    def test_product_creation(self):
        self.assertEqual(self.product.name, "bicicleta")

    def test_product_str(self):
        self.assertEqual(str(self.product), "bicicleta")

if __name__ == "__main__":
    unittest.main()
