n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

def go(sum, n):
    now = 0
    if sum > n:
        return 0
    if sum == n:
        return 1
    for i in range(1, 4):
        now += go(sum + i, n)
    return now

for num in a:
    print(go(0, num))
