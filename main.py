#10.10
class Laser():
    def does(cls):
        return "disintegrate"

class Claw():
    def does(self):
        return "crush"

class SmartPhone():
    def does(self):
        return "ring"

class Robot():
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()
    def does(self):
       return self.laser.does(), self.claw.does(), self.smartphone.does()

a = Robot()
print(a.does())
