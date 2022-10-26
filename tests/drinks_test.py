import unittest
from src.drinks import Drink

class TestDrink(unittest.TestCase):
    

    def setUp(self):
        self.drink = Drink("Mocha", 2.50, 40)

    def test_drink_has_name(self):
        self.assertEqual("Mocha", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(2.50, self.drink.price)