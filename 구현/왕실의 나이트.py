input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

move = [[-1, 2], [-1, -2], [-2, -1], [-2, 1], [1, -2], [1, 2], [2, -1], [2, 1]]
count = 0

for i in move:
    if row + i[0] > 8 or row + i[0] < 1 or col + i[1] > 8 or col + i[1] < 1:
        continue
    else:
        count += 1

print(count)
