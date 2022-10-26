class CoffeeShop:
    

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount

    def made_drinks(self):
        return len(self.drinks)

    def make_drink(self, drink_name):
        self.drinks.append(drink_name)
    
    def clear_drink(self):
        self.drinks.clear()

    def check_age(self, customer_age):
        if customer_age > 16:
            return True
        else:
            return False

    def check_customer_energy_level(self, customer_energy):
        if customer_energy <= 70:
            return True
        else:
            return False

