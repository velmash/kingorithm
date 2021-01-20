n = int(input())

check = n
count = 0

while True:
    temp = (n // 10) + (n % 10)
    result = (n % 10)*10 + (temp % 10)
    count += 1
    n = result
    if check == result:
        break

print(count)
