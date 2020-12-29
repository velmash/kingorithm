import sys
input = sys.stdin.readline
from collections import deque

# N: 도시 갯수, M: 도로 갯수, K: 거리 정보, X: 출발 도시 번호
n, m, k, x = map(int, input().split(" "))
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split(" "))
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

queue = deque()
queue.append(x)

while queue:
    now = queue.popleft()

    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            queue.append(next_node)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
