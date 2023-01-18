import random
def calculate_fee(args)-> dict:
    """
    놀이공원 요금 계산 프로그램
    :param args: ages
    :return: {'total': 전체 인원 수, 'adults': 어른 수, 'kids': 아이 수, 'total_money': 지불할 총 입장료}
    """
    total = 0
    adults = 0
    kids = 0
    for age in args:
        if 19 <= age:
            total = total + 10000
            adults = adults + 1
        else:
            total = total + 3000
            kids = kids + 1
    return {'total': len(args), 'adults': adults, 'kids': kids, 'total_money': total}


no_of_visitor = int(input("몇 분 이세요? "))
ages = [random.randint(1, 60) for age in range(no_of_visitor)]
results = calculate_fee(ages)
print(results)
print(f"{results['total']}명 방문 하셨고 어른{results['adults']}명, 아이{results['kids']}명. 지불할 총 입장료{results['total_money']}입니다.")
