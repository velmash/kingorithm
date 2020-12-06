x = 1
y = 1
ant_stage = []

for i in range(10):
    ant_stage.append(list(map(int, input().split())))

while(True):
    if ant_stage[y][x] == 2:
        ant_stage[y][x] = 9
        break
    elif ant_stage[y][x+1] == 1:
        if ant_stage[y+1][x] == 1:
            ant_stage[y][x] = 9
            break
        else:
            ant_stage[y][x] = 9
            y = y + 1
    elif x == 8 and y == 8:
        ant_stage[y][x] = 9
        break
    else:
        ant_stage[y][x] = 9
        x = x + 1
for i in range(len(ant_stage)):
    for j in range(len(ant_stage[i])):
        print(ant_stage[i][j], end=' ') if j != 10-1 else print(ant_stage[i][j], end = '\n')