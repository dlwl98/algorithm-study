from collections import deque
import sys
input = sys.stdin.readline

tc = int(input())
d = ((-1, 0), (1, 0), (0, 1), (0, -1))

for _ in range(tc):
    m, n = map(int, input().split())
    g = [list(input().rstrip()) for _ in range(n)]
    fireSet = set()
    sy = 0
    sx = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == '*':
                fireSet.add((i, j))
            if g[i][j] == '@':
                sy, sx = i, j
                g[i][j] = '.'
    
    def inRange(y, x):
        return 0 <= y < n and 0 <= x < m

    def fire():
        newFire = set()
        delFire = set()
        for i, j in fireSet:
            flag = True
            for dy, dx in d:
                ny = i + dy
                nx = j + dx
                if inRange(ny, nx) and g[ny][nx] == '.':
                    flag = False
                    newFire.add((ny, nx))
            if flag:
                delFire.add((i, j))
        for y, x in newFire:
            fireSet.add((y, x))
        for y, x in delFire:
            fireSet.remove((y, x))
        for y, x in fireSet:
            g[y][x] = '*'

    def isSafe(y, x):
        if g[y][x] == '*':
            return False
        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if not inRange(ny, nx):
                continue
            if g[ny][nx] == '*':
                return False
        return True

    def solution():
        curTick = 0
        q = deque()
        q.append((sy, sx, curTick))
        v = [[False] * m for _ in range(n)]
        v[sy][sx] = True
        while q:
            y, x, tick = q.popleft()
            if tick > curTick:
                fire()
                curTick +=1
            for dy, dx in d:
                ny = y + dy
                nx = x + dx
                if not inRange(ny, nx):
                    print(curTick + 1)
                    return
                if g[ny][nx] != '#' and not v[ny][nx] and isSafe(ny, nx):
                    v[ny][nx] = True
                    q.append((ny, nx, curTick + 1))
        print("IMPOSSIBLE")
    solution()
