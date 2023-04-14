from collections import deque

case = int(input())
for _ in range(case):
    n, m = map(int, input().split())
    g = [list(input()) for _ in range(n)]
    dic = dict()
    for asc in range(ord('A'), ord('Z') + 1):
        dic[chr(asc)] = False
    keys = list(input())
    for key in keys:
        if key != '0':
            dic[key.upper()] = True
    def refresh():
        flag = False
        v = [[False] * m for _ in range(n)]
        for i in range(n):
            tmp = []
            if i == 0 or i == n-1:
                tmp = range(m)
            else:
                tmp = [0, m-1]
            for j in tmp:
                if v[i][j]:
                    continue
                if g[i][j] == '*':
                    continue
                if g[i][j] != '.' and g[i][j] != '$':
                    if g[i][j] == g[i][j].upper() and not dic[g[i][j].upper()]:
                        continue
                    if g[i][j] != g[i][j].upper():
                        dic[g[i][j].upper()] = True

                q = deque()
                q.append((i, j))
                v[i][j] = True
                while q:
                    y, x = q.popleft()
                    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        ny = y + dy
                        nx = x + dx
                        if 0<=ny<n and 0<=nx<m and g[ny][nx] != '*' and not v[ny][nx]:
                            if g[ny][nx] == '.' or g[ny][nx] == '$':
                                q.append((ny, nx))
                                v[ny][nx] = True
                            else:
                                if g[ny][nx] == g[ny][nx].upper():
                                    if dic[g[ny][nx].upper()]:
                                        q.append((ny, nx))
                                        v[ny][nx] = True
                                else:
                                    if not dic[g[ny][nx].upper()]:
                                        dic[g[ny][nx].upper()] = True
                                        flag = True
                                    q.append((ny, nx))
                                    v[ny][nx] = True
        return flag

    while True:
        if not refresh():
            break
    
    result = 0
    v = [[False] * m for _ in range(n)]
    for i in range(n):
        tmp = []
        if i == 0 or i == n-1:
            tmp = range(m)
        else:
            tmp = [0, m-1]
        for j in tmp:
            if v[i][j]:
                continue
            if g[i][j] == '*':
                continue
            if g[i][j] != '.' and g[i][j] != '$':
                if g[i][j] == g[i][j].upper() and not dic[g[i][j].upper()]:
                    continue
                if g[i][j] != g[i][j].upper():
                    dic[g[i][j].upper()] = True

            q = deque()
            q.append((i, j))
            v[i][j] = True
            while q:
                y, x = q.popleft()
                if g[y][x] == '$':
                    result += 1
                for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ny = y + dy
                    nx = x + dx
                    if 0<=ny<n and 0<=nx<m and g[ny][nx] != '*' and not v[ny][nx]:
                        if g[ny][nx] == '.' or g[ny][nx] == '$':
                            q.append((ny, nx))
                            v[ny][nx] = True
                        else:
                            if g[ny][nx] == g[ny][nx].upper():
                                if dic[g[ny][nx].upper()]:
                                    q.append((ny, nx))
                                    v[ny][nx] = True
                            else:
                                q.append((ny, nx))
                                v[ny][nx] = True
    print(result)
