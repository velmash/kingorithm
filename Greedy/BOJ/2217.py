n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

result = 0
for i in range(len(arr)):
    if result <= arr[i] * (i+1):
        result = arr[i] * (i+1)

print(result)
