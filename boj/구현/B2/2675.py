n = int(input())

for i in range(n):
    r, p = input().split(" ")
    for j in p:
        print(j * int(r), end='')
    print()