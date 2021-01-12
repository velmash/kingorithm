n = list(input())

if len(n) % 2 == 1:
    print("fail")
else:
    front = n[0:int(len(n)/2)]
    end = n[int(len(n)/2):int(len(n))]

    list1 = []
    list2 = []

    for i in front:
        list1.append(int(i))
    for i in end:
        list2.append(int(i))

    if sum(list1) == sum(list2):
        print("LUCKY")
    else:
        print("READY")

# 교재 답안
'''
n = input()
length = len(n) # 점수 값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수의 합 더하기
for i in range(length // 2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수의 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
    print("LUCKY")
else:
    print("READY")
'''