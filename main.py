import math
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_area(self):
        print('도형의 면적을 출력합니다.')

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
    def get_area(self):
        return math.pi * self.radius *self.radius

class Square(Shape):
    def __init__(self, x, y, width, length):
        super().__init__(x, y)
        self.width = width
        self.length = length
    def get_area(self):
        return math.pi * self.width * self.length

c1 = Circle(100, 100, 10.0)
c2 = Circle(50, 50, 2.0)
r1 = Square(100, 50, 5, 2)

print(f'사각형의 좌표는 x:{r1.x}, y:{r1.y}이고 넓이는 {r1.get_area()}')