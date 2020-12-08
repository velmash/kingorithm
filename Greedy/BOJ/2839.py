kilogram = int(input())
count = 0

while True:
    if kilogram % 5 != 0:
        kilogram -= 3
        count += 1
    elif kilogram % 5 == 0:
        count += kilogram // 5
        break
    if kilogram < 0:
        count = -1
        break

print(count)