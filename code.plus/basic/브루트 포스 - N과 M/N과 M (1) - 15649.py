n, m = map(int, input().split())
check = [False] * (n + 1)
a = [0] * m

def go(index, n, m):
    if index == m:
        print(' '.join(map(str, a)))
        return

    for i in range(1, n + 1):
        if check[i] == True:
            continue
        check[i] = True
        a[index] = i
        go(index + 1, n, m)
        check[i] = False


go(0, n, m)
