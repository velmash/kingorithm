# 2보다 큰 모든 짝수는 두 소수의 합으로 표현 가능하

# 에라토스테네스의 체
MAX = 1000000
check = [0]*(MAX+1)
prime = []

check[0] = True
check[1] = True

for i in range(2, MAX + 1):
    if not check[i]:
        prime.append(i)
        j = i + i
        while j < MAX:
            check[j] = True
            j += i

while True:
    n = int(input())

    if n == 0:
        break
    for num in prime:
        if not check[n - num]:
            print("{0} = {1} + {2}".format(n, num, n - num))
            break




