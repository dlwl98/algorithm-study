di = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
n, m, k = map(int, input().split())
g = [[[] for _ in range(n)] for _ in range(n)]
balls = [list(map(int, input().split())) for _ in range(m)]

for ball in balls:
    y, x, m, s, d = ball
    g[y-1][x-1].append([m, s, d])

def go():
    tmp = []
    for y in range(n):
        for x in range(n):
            while g[y][x]:
                m, s, d = g[y][x].pop()
                dy, dx = di[d][0] * s, di[d][1] * s
                ny = y + dy
                nx = x + dx
                tmp.append([ny % n, nx % n, m, s, d])

    for y, x, m, s, d in tmp:
        g[y][x].append([m, s, d])

    for y in range(n):
        for x in range(n):
            l = len(g[y][x])
            if l >= 2:
                _m, _s, _d = 0, 0, g[y][x][0][2] % 2
                flag = 0
                while g[y][x]:
                    m, s, d = g[y][x].pop()
                    _m += m
                    _s += s
                    if d % 2 != _d:
                        flag = 1
                _m //= 5
                _s //= l
                if _m:
                    for i in (0, 2, 4, 6):
                        g[y][x].append([_m, _s, i + flag])

for _ in range(k):
    go()

result = 0
for y in range(n):
    for x in range(n):
        for m, s, d in g[y][x]:
            result += m

print(result)
