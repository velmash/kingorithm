# 나중에 잘하게되면,,

def solution(food_times, k):
    answer = 0
    return answer


food_times = [3, 1, 2]
k = 5

total_time = 0
pass_time = 0

for i in food_times:
    total_time += i

for i in range(k):
    if k > total_time:
        print(-1)
    else:
        if food_times[i % len(food_times)] == 0:
           print('hi')

