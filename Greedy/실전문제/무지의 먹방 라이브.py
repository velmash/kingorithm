# 정확성 풀이

from itertools import cycle


def solution(food_times, k):
    index_array = cycle([i for i in range(len(food_times))])
    done = False
    counter = 0
    while done is False:
        index = next(index_array)
        if sum(food_times) == 0:
            return -1
        if food_times[index] > 0:
            counter += 1
            food_times[index] -= 1
        done = True if counter == k + 1 else False
    return index + 1


print(solution([3, 1, 2], 5))
