#6.3
guess_me=5
number=1

for i in range(1,11):
    if guess_me>number:
        print("too low")
        number=number+1

    elif guess_me<number:
        print("oops")
        number=number+1

    else:
        print('found it')
        break