# -*- coding: utf-8 -*-

n = 10
a = [0] * n
print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 여덟 번째 원소만 출력
print(a[7])

# 뒤에서 세 번째 원소 출력
print(a[-3])

# 슬라이싱
# 끝 인덱스는 실제 인덱스보다 1을 더 크게 설정
# 두 번째 원소부터 네 번째 원소까지
print(a[1 : 4])

# 리스트 컴프리헨션
# 대괄호 안에 조건문과 반목문을 적용하여 리스트를 초기화 할 수 있다.
# 0부터 9까지의 수를 포한하는 리스
array = [i for i in range(10)]
print(array)

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 1부터 9까지의 수들의 제곱 값을 포함하는 리스트
array = [i*i for i in range(1,10)]
print(array)

# N X M 크기의 2차원 리스트를 한 번에 초기화 하는법
# array = [[0] * m for _ in range(n)]

# 딕셔너리
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
value_list = data.values()
print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])



# 집합 자료형
# 초기화 방법 1
data = set([1, 1, 2, 3, 4, 5, 5])
print(data)

# 초기화 방법 2
data = { 1, 1, 2, 3, 4, 4, 4, 5, 6}
print(data)

# 새로운 원소 추가
data.add(4)

# 새로운 원소 여러개 추가
data.update([7,8])

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)

# input() 함수는 한 줄의 문자열을 입력받는 함수
# map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
# 공백을 기준으로 구분된 데이터를 입력 받을 때
# list(map(int, input().split()))
# 공백을 기준으로 구분된 데이터의 개수가 많지 않다면
# a, b, c = map(int, input().split())

# 데이터의 개수 입력
# n = int(input())
# 각 데이터를 공백을 기준으로 구분하여 입력
# data = list(map(int, input().split()))
# print(data)

# import sys

# 빠르게 문자열 입력 받기
# data = sys.stdin.readline().rstrip()
# print(type(data))

answer = 7
print(f"정답은 {answer}입니다.")

def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var

a, b, c, d = operator(7, 3)
print(a, b, c, d)


# 람다 표현식
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))
# 위와 아래는 같
print(sorted(array, key=lambda x: x[1]))


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a+b, list1, list2)
print(list(result))




# 코딩테스트에 유용한 라이브러리

# 내장함수
# sum()
result = sum([1, 2, 3, 4, 5])

# min(), max()
min_result = min(7, 3, 6, 2)
max_result = max(7, 3, 6, 2)

#eval()
result = eval("(3+5)*7")

#sorted()
result = sorted(([9, 1, 8, 5, 4]))
reverse_result = sorted(([9, 1, 8, 5, 4]), reverse=True)

#sorted() with key
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
result = sorted(array, key=lambda x: x[1], reverse=True)




# 순열과 조합
from itertools import permutations

data = ['A', 'B', 'C']

result = list(permutations(data, 3)) # 모든 브루트 포스 - 순열 구하기
print(result)

from itertools import combinations
result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기
print(result)


# 중복 브루트 포스 - 순열
from itertools import product
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 브루트 포스 - 순열 구하기(중복 허용)

# 중복 조합
from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)



# Counter - 등장 횟수 세는 기능 제공
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue']) # blue가 있는 수 출


# 최대공약수는 math라이브러리의 gcd() 함수
import math
# 최소 공배수(LCM)을 구하는 함수
def lcm(a, b):
    return a*b // math.gcd(a, b)

a = 21
b = 14

print(math.gcd(a, b)) # 최대공약수 계산
print(lcm(a, b)) # 최소공배수 계산

