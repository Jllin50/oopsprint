import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


def convert(lst):
    lst = str(lst)
    return (lst.split())


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_explode(self):
        """Tests the explode methods"""
        prod = Product('Shiny Table', 35, 500, .1)
        self.assertEqual(prod.explode(), '...BABOOM!!')

    def test_stealability(self):
        """Test the stealability method"""
        prod = Product('Shiny Table', 35, 500, .1)
        self.assertEqual(prod.stealability(), 'Not so stealable...')


class AcmeReportTests(unittest.TestCase):
    """Testing the acme report file"""
    def test_default_num_products(self):
        """Tests the number of products in the report"""
        prod_list = generate_products()
        self.assertEqual(len(prod_list), 30)

    def test_legal_names(self):
        """Tests that the names are legal"""
        prod_list = generate_products()
        product_names = []
        for prod in prod_list:
            product_names.append(prod.name)
        cleaned_names = []
        for name in product_names:
            name_words = convert(name)
            for word in name_words:
                cleaned_names.append(word)
        cleaned_set = set(cleaned_names)
        cleaned_names = list(cleaned_set)
        cleaned_names.sort()
        combined_options = ADJECTIVES + NOUNS
        combined_options.sort()
        self.assertEqual(cleaned_names, combined_options)

if __name__ == '__main__':
    unittest.main()
