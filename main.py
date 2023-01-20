# 10.3
class Thing3():
    def __init__(self):
        self.letters = 'xyz'


print(Thing3.letters)  #클래스를 만들지 못했기 때문에 __init__에 접근하지 못한다.
print(Thing3().letters)  #init에 접근할때는 다음과 같이 ()클래스를 만들고 불러오기
