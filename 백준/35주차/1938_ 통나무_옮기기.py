from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
g = [list(input().rstrip()) for _ in range(n)]
v = [[[10**9] * 2 for _ in range(n)] for _ in range(n)]

def getS():
    global cnt
    sy, sx, sf = 0, 0, 0
    for i in range(n):
        for j in range(n):
            if g[i][j] == 'B':
                if cnt == 1:
                    ty, tx = sy, sx
                    sy, sx = i, j
                    if ty != sy:
                        sf = 1
                    return sy, sx, sf
                else:
                    cnt += 1
                    sy, sx = i, j
def getE():
    global cnt
    ey, ex, ef = 0, 0, 0
    for i in range(n):
        for j in range(n):
            if g[i][j] == 'E':
                if cnt == 1:
                    ty, tx = ey, ex
                    ey, ex = i, j
                    if ty != ey:
                        ef = 1
                    return ey, ex, ef
                else:
                    cnt += 1
                    ey, ex = i, j
cnt = 0
sy, sx, sf = getS()
cnt = 0
ey, ex, ef = getE()

q = deque()
q.append([sy, sx, sf, 0])
v[sy][sx][sf] = 0
while q:
    y, x, f, cnt = q.popleft()
    if [y, x, f] == [ey, ex, ef]:
        print(cnt)
        exit()

    if f == 1:
        if x > 0 and g[y-1][x-1] != '1' and g[y][x-1] != '1' and g[y+1][x-1] != '1':
            if v[y][x-1][f] > cnt + 1:
                v[y][x-1][f] = cnt + 1
                q.append([y, x-1, f, cnt + 1])
        if x < n-1 and g[y-1][x+1] != '1' and g[y][x+1] != '1' and g[y+1][x+1] != '1':
            if v[y][x+1][f] > cnt + 1:
                v[y][x+1][f] = cnt + 1
                q.append([y, x+1, f, cnt + 1])
        if y > 1 and g[y-2][x] != '1':
            if v[y-1][x][f] > cnt + 1:
                v[y-1][x][f] = cnt + 1
                q.append([y-1, x, f, cnt + 1])
        if y < n-2 and g[y+2][x] != '1':
            if v[y+1][x][f] > cnt + 1:
                v[y+1][x][f] = cnt + 1
                q.append([y+1, x, f, cnt + 1])
        if x > 0 and g[y-1][x-1] != '1' and g[y][x-1] != '1' and g[y+1][x-1] != '1':
            if x < n-1 and g[y-1][x+1] != '1' and g[y][x+1] != '1' and g[y+1][x+1] != '1':
                if v[y][x][0] > cnt + 1:
                    v[y][x][0] = cnt + 1
                    q.append([y, x, 0, cnt + 1])
    else :
        if x > 1 and g[y][x-2] != '1':
            if v[y][x-1][f] > cnt + 1:
                v[y][x-1][f] = cnt + 1
                q.append([y, x-1, f, cnt + 1])
        if x < n-2 and g[y][x+2] != '1':
            if v[y][x+1][f] > cnt + 1:
                v[y][x+1][f] = cnt + 1
                q.append([y, x+1, f, cnt + 1])
        if y > 0 and g[y-1][x-1] != '1' and g[y-1][x] != '1' and g[y-1][x+1] != '1':
            if v[y-1][x][f] > cnt + 1:
                v[y-1][x][f] = cnt + 1
                q.append([y-1, x, f, cnt + 1])
        if y < n-1 and g[y+1][x-1] != '1' and g[y+1][x] != '1' and g[y+1][x+1] != '1':
            if v[y+1][x][f] > cnt + 1:
                v[y+1][x][f] = cnt + 1
                q.append([y+1, x, f, cnt + 1])
        if y > 0 and g[y-1][x-1] != '1' and g[y-1][x] != '1' and g[y-1][x+1] != '1':
            if y < n-1 and g[y+1][x-1] != '1' and g[y+1][x] != '1' and g[y+1][x+1] != '1':
                if v[y][x][1] > cnt + 1:
                    v[y][x][1] = cnt + 1
                    q.append([y, x, 1, cnt + 1])

print(0)
