# 10.7
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return (f"name: {self.name}, symbol: {self.symbol}, number: {self.number}")

hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen)  #이거는 앞에 hyerogen.dump()처럼 함수를 호출하지 않아도 자동으로 반환되서 문자열이 출력된다.