nan = []
for _ in range(9):
    nan.append(int(input()))

sum_s = sum(nan)
noAnswer1 = 0
noAnswer2 = 0

for i in range(8):
    for j in range(i+1, 9):
        if (sum_s - nan[i] - nan[j]) == 100:
            noAnswer1 = nan[i]
            noAnswer2 = nan[j]
            break

nan.sort()
nan.remove(noAnswer1)
nan.remove(noAnswer2)

for i in nan:
    print(i)
