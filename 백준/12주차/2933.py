from collections import deque

r, c = map(int, input().split())
g = [list(input()) for _ in range(r)]
n = int(input())
sticks = list(map(int, input().split()))


def fall():
    v = [[False] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if not v[i][j] and g[i][j] == 'x':
                clusters = set()
                q = deque()
                v[i][j] = True
                q.append([i, j])
                clusters.add((i, j))
                while q:
                    y, x = q.popleft()
                    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        ny = y + dy
                        nx = x + dx
                        if 0 <= ny < r and 0 <= nx < c and not v[ny][nx] and g[ny][nx] == 'x':
                            v[ny][nx] = True
                            q.append([ny, nx])
                            clusters.add((ny, nx))
                flag = True
                for cluster in clusters:
                    y, x = cluster
                    if y == r - 1:
                        flag = False
                        break
                    if g[y + 1][x] == 'x' and (y + 1, x) not in clusters:
                        flag = False
                        break

                if flag:
                    count = 10 ** 9
                    for y, x in clusters:
                        if (y + 1, x) not in clusters:
                            for k in range(1, count + 1):
                                if y + k == r:
                                    count = min(count, k - 1)
                                    break
                                if g[y + k][x] == 'x' and (y + k, x) not in clusters:
                                    count = min(count, k - 1)
                                    break

                    tmp = set()
                    for y, x in clusters:
                        tmp.add((y + count, x))
                    for y, x in clusters:
                        g[y][x] = '.'
                    for y, x in tmp:
                        g[y][x] = 'x'

                    return True
    return False


for i in range(len(sticks)):
    stick = sticks[i]
    if i % 2 == 0:
        for j in range(c):
            if g[r - stick][j] == 'x':
                g[r - stick][j] = '.'
                fall()
                break
    else:
        for j in range(1, c + 1):
            if g[r - stick][c - j] == 'x':
                g[r - stick][c - j] = '.'
                fall()
                break

for a in g:
    for b in a:
        print(b, end='')
    print()
