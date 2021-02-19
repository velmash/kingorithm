n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

a = [0] * m


def go(index, start, n, m):
    if start == m:
        print(' '.join(map(str, a)))
        return
    if index == n:
        return
    a[start] = nums[index]
    go(index, start + 1, n, m)
    a[start] = 0
    go(index + 1, start, n, m)


go(0, 0, n, m)
