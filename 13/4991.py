from sys import stdin
from collections import deque
from itertools import permutations

while True:
    w, h = map(int, stdin.readline().split())
    if w == 0 and h == 0:
        break
    g = [list(stdin.readline().rstrip()) for _ in range(h)]
    sy, sx = 0, 0
    dirty = []

    for i in range(h):
        for j in range(w):
            if g[i][j] == 'o':
                sy, sx = i, j
            elif g[i][j] == '*':
                dirty.append((i, j))

    def in_range(y, x):
        return 0 <= y < h and 0 <= x < w

    def min_way(y1, x1, y2, x2):
        v = [[False] * w for _ in range(h)]
        q = deque()
        q.append((y1, x1, 0))
        v[y1][x1] = True
        while q:
            y, x, cnt = q.popleft()
            if y == y2 and x == x2:
                return cnt
            for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ny = y + dy
                nx = x + dx
                if in_range(ny, nx) and g[ny][nx] != 'x' and not v[ny][nx]:
                    v[ny][nx] = True
                    q.append((ny, nx, cnt + 1))
        return 10**9

    start = []
    for y, x in dirty:
        tmp = min_way(sy, sx, y, x)
        start.append(tmp)

    if max(start) == 10**9:
        print(-1)
        continue

    k = len(dirty)
    way = [[-1] * k for _ in range(k)]
    for i in range(len(dirty)):
        for j in range(len(dirty)):
            if i == j:
                way[i][j] = 0
            elif way[j][i] != -1:
                way[i][j] = way[j][i]
            else:
                way[i][j] = min_way(dirty[i][0], dirty[i][1], dirty[j][0], dirty[j][1])

    result = 10**9
    for per in permutations(range(k), k):
        tmp = start[per[0]]
        for i in range(1, k):
            tmp += way[per[i-1]][per[i]]

        result = min(result, tmp)

    print(result)
