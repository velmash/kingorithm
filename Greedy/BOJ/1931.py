n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split(' '))))

data.sort(key=lambda x: (x[1], x[0]))

count = 1

end_time = data[0][1]

for i in range(1, n):
    if data[i][0] >= end_time:
        count += 1
        end_time = data[i][1]

print(count)
