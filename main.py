# 10.6
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(f"name: {self.name}, symbol: {self.symbol}, number: {self.number}")

hydrogen = Element('Hydrogen', 'H', 1)
hydrogen.dump()