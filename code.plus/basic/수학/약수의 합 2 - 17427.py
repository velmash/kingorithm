n = int(input())
count = 1
result = 0

while n >= count:
    m = n // count
    result += m * count
    count += 1

print(result)
