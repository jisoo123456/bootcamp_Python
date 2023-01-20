# class
class Pokemon:
    def __init__(self, owner, skills):
        self.owner = owner
        self.skills = skills.split('/')  #split자체가 리스트로 반환
        print(f'포켓몬 생성됨:', end=' ')

    def info(self):
        print(f"{self.owner}의 포켓몬이 사용 가능한 스킬")
        for skill in self.skills:
            print(skill)

    def attack(self, idx):
        print(f'{self.skills[idx]} 공격 시전!')

class Pikachu(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = '피카츄'  #self 안 달아주면 밑에 attrack함수에서 self.name아니고 name으로 하면 못 받음
        print(f'피카츄')
    def attack(self, idx):
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격(전기) 시전!')

class Ggoboogi(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "꼬부기"
        print(f'꼬부기')
    def attack(self, idx):
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격(물) 시전!')
    def swim(self):
        print(f'{self.name}이 수영을 합니다.')

pk1 = Pikachu('한지우', '50만 볼트/100만 볼트/번개')
ggo1 = Ggoboogi('오바람', '고속스핀/거품/몸통박치기')
ggo1.swim()
# pk1.info()
# ggo1.info()
ggo1.attack(1)
pk1.attack(1)
