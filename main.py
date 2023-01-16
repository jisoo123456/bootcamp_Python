#6.2

guess_me=7
number=1

while True:
    if guess_me>number:
        print("too low")
        number=number+1

    elif guess_me<number:
        print("oops")
        number=number+1

    else:
        print('found it')
        break