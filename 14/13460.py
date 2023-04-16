from collections import deque

n, m = map(int, input().split())
g = [list(input()) for _ in range(n)]
di = ((-1, 0), (1, 0), (0, 1), (0, -1))
R = [0, 0]
B = [0, 0]
for i in range(n):
    for j in range(m):
        if g[i][j] == 'R':
            g[i][j] = '.'
            R = [i, j]
        elif g[i][j] == 'B':
            g[i][j] = '.'
            B = [i, j]

def go(y, x, d, ball):
    if g[y][x] == 'O':
        return [y, x]
    dy, dx = di[d]
    ny = y
    nx = x
    while True:
        ny += dy
        nx += dx
        if ny == ball[0] and nx == ball[1]:
            break
        if g[ny][nx] == 'O':
            ny += dy
            nx += dx
            break
        if g[ny][nx] == '#':
            break
    return [ny - dy, nx - dx]
    
q = deque()
q.append((R[0], R[1], B[0], B[1], 0))
while q:
    ry, rx, by, bx, cnt = q.popleft()
    if cnt > 9:
        print(-1)
        exit()
    for d in (0, 1, 2, 3):
        nry, nrx, nby, nbx = ry, rx, by, bx
        nry, nrx = go(nry, nrx, d, [nby, nbx])
        nby, nbx = go(nby, nbx, d, [nry, nrx])
        nry, nrx = go(nry, nrx, d, [nby, nbx])
        if g[nby][nbx] == 'O':
            continue
        if g[nry][nrx] == 'O':
            nby, nbx = go(nby, nbx, d, [0, 0])
            if g[nby][nbx] == 'O':
                continue
            else:
                print(cnt + 1)
                exit()
        if nry != ry or nrx != rx or nby != by or nbx != bx:
            q.append((nry, nrx, nby, nbx, cnt + 1))
print(-1)
