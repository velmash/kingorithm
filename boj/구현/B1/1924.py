x, y = map(int, input().split())

a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
c = 2

sumD = 0
for i in range(x):
    # a에 i월이 있으면 31을 더한다.
    if i in a:
        sumD += 31
    # b에 i월이 있으면 30을 더한다.
    elif i in b:
        sumD += 30
    # c가 2월이면 28을 더한다.
    elif i == c:
        sumD += 28

# 나머지 y일을 더한다.
sumD += y

if sumD % 7 == 0:
    print('SUN')
elif sumD % 7 == 1:
    print('MON')
elif sumD % 7 == 2:
    print('TUE')
elif sumD % 7 == 3:
    print('WED')
elif sumD % 7 == 4:
    print('THU')
elif sumD % 7 == 5:
    print('FRI')
elif sumD % 7 == 6:
    print('SAT')