#입력된 두 수 사이의 소수 출력

start=int(input('start number: '))
end=int(input('end number: '))

if end<start:
    start, end= end, start

for i in range(start, end+1):

    if i <=1:
        continue
    for k in range(2,i):
        if i%k ==0:
            break
    else:
        print(i, end=' ')