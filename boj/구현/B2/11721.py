n = input()

count = 0

for i in n:
    if count < 9:
        print(i, end='')
        count += 1
    else:
        count = 0
        print(i)
