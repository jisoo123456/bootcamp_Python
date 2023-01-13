import random

guess=int(input("1~10사이의 숫자를 선택하여 입력하시오."))
secret=random.randint(1,10)

if secret > guess:
    print("too low")

if secret < guess:
    print("too high")

if secret == guess:
    print("just right")

print(secret)