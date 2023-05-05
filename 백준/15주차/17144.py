r, c, t = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(r)]
di = ((-1, 0), (0, 1), (1, 0), (0, -1))
top = 0
bottom = 0


for y in range(2, r):
    if g[y][0] == -1:
        top = y
        bottom = y+1
        break

def inRange(y, x):
    return 0 <= y < r and 0 <= x < c

def spread():
    tmp = []
    for y in range(r):
        for x in range(c):
            if g[y][x] > 0:
                cnt = 0
                for dy, dx in di:
                    ny = y + dy
                    nx = x + dx
                    if inRange(ny, nx):
                        if ny == top and nx == 0:
                            continue
                        if ny == bottom and nx == 0:
                            continue
                        tmp.append([ny, nx, g[y][x] // 5])
                        cnt += 1
                g[y][x] -= g[y][x] // 5 * cnt
    for y, x, val in tmp:
        g[y][x] += val

def topMove():
    for y in range(top-2, -1, -1):
        g[y+1][0] = g[y][0]
    for x in range(1, c):
        g[0][x-1] = g[0][x]
    for y in range(1, top+1):
        g[y-1][c-1] = g[y][c-1]
    for x in range(c-2, 0, -1):
        g[top][x+1] = g[top][x]
    g[top][1] = 0

def bottomMove():
    for y in range(bottom+2, r):
        g[y-1][0] = g[y][0]
    for x in range(1, c):
        g[r-1][x-1] = g[r-1][x]
    for y in range(r-2, bottom-1, -1):
        g[y+1][c-1] = g[y][c-1]
    for x in range(c-2, 0, -1):
        g[bottom][x+1] = g[bottom][x]
    g[bottom][1] = 0

for _ in range(t):
    spread()
    topMove()
    bottomMove()

result = 0
for a in g:
    result += sum(a)
print(result + 2)
