ex = list(input())
alpha_list = []
num_list = []

for i in ex:
    if ord(i) >= 65 and ord(i) <= 90:
        alpha_list.append(i)
    else:
        num_list.append(int(i))

alpha_list.sort()
num_list.sort()

print(alpha_list, num_list)

for a in alpha_list:
    print(a, end="")
print(sum(num_list))


# 교재 답안
'''
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))
'''