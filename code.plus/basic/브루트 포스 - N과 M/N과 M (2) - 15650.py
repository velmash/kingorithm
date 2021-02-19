n, m = map(int, input().split())
check = [False] * (n + 1)
a = [0] * m

def go(index, start, n, m):
    if index == m:
        print(" ".join(map(str, a)))
        return
    for i in range(start, n+1):
        if check[i] == True:
            continue
        a[index] = i
        check[i] = True
        start = i
        go(index+1, start, n, m)
        check[i] = False

go(0, 1, n, m)
