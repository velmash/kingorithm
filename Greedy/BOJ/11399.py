n = int(input())
p = list(map(int, input().split(' ')))
p.sort()

temp = 0
sumlist = []

for i in p:
    temp += i
    sumlist.append(temp)

print(sum(sumlist))
