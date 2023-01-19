cnts = 0  #for문 안에 cnts를 넣으면 반복문이 돌때마다 0으로 초기화가 됨.
def get_odds():
    for num in range(10):
        if num % 2 == 1:
            yield num  #yied가 아닌 return을 써버리면 1만 return 받고 끝나서 odds는 정수가 됨.

odds = get_odds()
for i in odds:
    cnts = cnts + 1
    if cnts == 3:
        print(i)
