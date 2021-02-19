n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
c = [[False] * m for _ in range(n)]

answer = 0
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def go(count, sum):
    if count == k:
        global answer
        if answer < sum:
            answer = sum
        return

    for x in range(n):
        for y in range(m):
            if c[x][y]:
                continue
            ok = True
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < n and 0 <= ny < m: # board 안에 있다면
                    if c[nx][ny]:
                        ok = False
            if ok:
                c[x][y] = True
                go(count + 1, sum + board[x][y])
                c[x][y] = False

go(0, 0)
print(answer)
