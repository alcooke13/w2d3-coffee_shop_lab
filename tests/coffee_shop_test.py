import unittest
from src.drinks import Drink
from src.coffee_shop import CoffeeShop
from src.customer import Customer

class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self):
        self.coffee_shop = CoffeeShop("The Prancing Pony", 100.00)
        self.drinks = Drink("Mocha", 2.50, 40)
        self.customer1 = Customer("Jeff Bridges", 150, 21, 50)
        self.customer2 = Customer("Sally Rogers", 25, 15, 80)

    def test_coffee_shop_has_name(self):
        self.assertEqual("The Prancing Pony", self.coffee_shop.name)

    def test_increase_till(self):
        self.coffee_shop.increase_till(20.00)
        self.assertEqual(120.00, self.coffee_shop.till)

    def test_drinks_stock_level(self):
        self.assertEqual(0, self.coffee_shop.made_drinks())

    def test_can_make_drink(self):
        self.coffee_shop.make_drink(self)
        self.assertEqual(1, self.coffee_shop.made_drinks())

    def test_can_clear_drink(self):
        self.coffee_shop.make_drink(self.drinks)
        self.coffee_shop.clear_drink()
        self.assertEqual(0, self.coffee_shop.made_drinks())

    def test_check_age_over_16(self):
        customer_age = self.coffee_shop.check_age(self.customer1.age)
        self.assertEqual(True, customer_age)

    def test_check_age_under_16(self):
        customer_age = self.coffee_shop.check_age(self.customer2.age)
        self.assertEqual(False, customer_age)

    def test_check_customer_energy_level_serve(self):
        customer_energy = self.coffee_shop.check_customer_energy_level(self.customer1.energy_level)
        self.assertEqual(True, customer_energy)

    def test_check_customer_energy_level_no(self):
        customer_energy = self.coffee_shop.check_customer_energy_level(self.customer2.energy_level)
        self.assertEqual(False, customer_energy)
        


        