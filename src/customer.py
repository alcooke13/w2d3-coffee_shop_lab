class Customer:

    def __init__(self, name, wallet, age, energy_level):
        self.name = name
        self.wallet = wallet
        self.drink_count = []
        self.age = age
        self.energy_level = energy_level

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def add_drink(self, drink_name):
        self.drink_count.append(drink_name)
        

    def check_drink_count(self):
        return len(self.drink_count)
    
    def increase_energy_level(self, amount):
        self.energy_level += amount

