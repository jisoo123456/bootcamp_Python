def isprime(n):
    if n <= 1:
        return False

    for k in range(2, n):
        if n % k == 0:
            return False

    else:
        return True

start = int(input("input start number:"))
end = int(input("input end number:"))

if end < start:
    start, end = end, start

for i in range(start, end+1):
    if isprime(i):
        print(i, end=' ')
