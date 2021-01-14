t = int(input())
a, b, c = 300, 60, 10
count_list = [0, 0, 0]

while t != 0:
    if t >= a:
        count_list[0] += 1
        t -= a
        continue
    elif t >= b:
        count_list[1] += 1
        t -= b
        continue
    elif t >= c:
        count_list[2] += 1
        t -= c
        continue
    else:
        count_list[0] = 0
        count_list[1] = 0
        count_list[2] = 0
        break
if sum(count_list) > 0 :
    for i in count_list:
        print(i, end=" ")
else:
    print(-1)