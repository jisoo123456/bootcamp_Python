# 10.1
class Thing():
    pass

example = Thing()
print(Thing)  #출력값은 <class '__main__.Thing'> (class이기 때문)
print(example)  #출력값은 <__main__.Thing object at 0x000002104AEBA1C0>으로 다르다.