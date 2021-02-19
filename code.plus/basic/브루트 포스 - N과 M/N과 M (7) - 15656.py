n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

a = [0] * m

def do(index, start, n, m):
    if index == m:
        print(' '.join(map(str, a)))
        return
    for i in range(n):
        if start != m:
            a[index] = nums[i]
            do(index + 1, start + 1, n, m)


do(0, 0, n, m)