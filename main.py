# 9.3
def test(func):
    def test_a(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print(result)
        print('end')
        return result
    return test_a

@test
def plus(a, b):
    return a + b

plus(3, 4)

@test
def minus(a, b):
    return a -b

minus(5, 2)