def calculate():
    x = 1
    y = 2
    temp = 0
    def add_sub(n):
        nonlocal temp
        temp = temp + x - y
        return temp
    return add_sub

c1 = calculate()  #add_sub함수의 주소/ 즉 c1은 add_sub이다.
for i in range(5):
    print(c1(i))