def next_per(a):
    i = len(a) - 1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1

    while a[j] <= a[i-1]:
        j -= 1

    a[i-1], a[j] = a[j], a[i-1]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True

def sum(a):
    ans = 0
    for i in range(1, len(a)):
        ans += abs(a[i] - a[i-1])
    return ans



n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0

while True:
    temp = sum(a)
    ans = max(ans, temp)
    if not next_per(a):
        break
print(ans)