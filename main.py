# generator

def a():
    yield 1
    yield 2
    yield 3

def b():
    return 1  #1을 return 하고 종류/뒤에는 실행되지 않음
    return 2
    return 3

print(a(), b())

for i in a():
    print(i)