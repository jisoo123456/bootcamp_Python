#prime_number

number = int(input("input number:"))
counts = 0

k=1
while k <= number:
    if number % k == 0:
        counts = counts+1
    k=k+1

if counts ==2 :
    print(f'{number} is prime number')
else:
    print(f'{number}is NOT prime number')

