# 10.8
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    @property
    def Name(self):
        return self.name
    @property
    def Symbol(self):
        return self.symbol
    @property
    def Number(self):
        return self.number

hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen.Name)
print(hydrogen.Symbol)
print(hydrogen.Number)