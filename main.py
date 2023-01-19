# 9.2
def get_odds():
    for numb in range(10):
        if numb % 2 != 0:
            yield numb

a = get_odds()

count = 0
for i in get_odds():
    count = count +1
    if count == 3:
        print(i)