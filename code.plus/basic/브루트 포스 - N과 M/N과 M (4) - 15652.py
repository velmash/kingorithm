n, m = map(int, input().split())
a = [0] * m

def go(index, start, n, m):
    if index == m:
        print(' '.join(map(str, a)))
        return
    for i in range(start, n + 1):
        a[index] = i
        start = i
        go(index + 1, start, n, m)

go(0, 1, n, m)