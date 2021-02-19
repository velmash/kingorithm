n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

check = [False] * n
a = [0] * m

def do(index, n, m):
    if index == m:
        print(' '.join(map(str, a)))
        return
    for i in range(n):
        if check[i] == False:
            check[i] = True
            a[index] = nums[i]
            do(index + 1, n, m)
            check[i] = False

do(0, n, m)