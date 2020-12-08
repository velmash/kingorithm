n, k = map(int, input().split(' '))
coin = []
for i in range(n):
    coin.append(int(input()))

index = -1
for i in coin:
    if i <= k:
        index += 1

result = 0

while index != -1:
    result += k // coin[index]
    k %= coin[index]
    index -= 1

print(result)