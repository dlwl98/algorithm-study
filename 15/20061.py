n = int(input())
g = [[False] * 10 for _ in range(10)]

def shift(flag, removed):
    if flag:
        for i in range(removed - 1, 3, -1):
            for j in range(4):
                g[j][i+1] = g[j][i]
                g[j][i] = False
    else:
        for i in range(removed - 1, 3, -1):
            for j in range(4):
                g[i+1][j] = g[i][j]
                g[i][j] = False

def putBlue(t, y, x):
    if t == 1:
        for i in range(6, 10):
            if g[y][i]:
                g[y][i-1] = True
                return
        g[y][9] = True
    elif t == 2:
        for i in range(6, 10):
            if g[y][i]:
                g[y][i-1] = True
                g[y][i-2] = True
                return
        g[y][8] = True
        g[y][9] = True
    else:
        for i in range(6, 10):
            if g[y][i] or g[y+1][i]:
                g[y][i-1] = True
                g[y+1][i-1] = True
                return
        g[y][9] = True
        g[y+1][9] = True

def putRed(t, y, x):
    if t == 1:
        for i in range(6, 10):
            if g[i][x]:
                g[i-1][x] = True
                return
        g[9][x] = True
    elif t == 2:
        for i in range(6, 10):
            if g[i][x] or g[i][x+1]:
                g[i-1][x] = True
                g[i-1][x+1] = True
                return
        g[9][x] = True
        g[9][x+1] = True
    else:
        for i in range(6, 10):
            if g[i][x]:
                g[i-1][x] = True
                g[i-2][x] = True
                return
        g[8][x] = True
        g[9][x] = True

def remove1(flag):
    for i in range(9, 5, -1):
        cnt = 0
        for j in range(4):
            if flag:
                if g[j][i]:
                    cnt += 1
            else:
                if g[i][j]:
                    cnt += 1
        if cnt == 4:
            shift(flag, i)
            return True
    return False

def remove2(flag):
    cnt = 0
    for i in (5, 4):
        for j in range(4):
            if flag:
                if g[j][i]:
                    cnt += 1
                    break
            else:
                if g[i][j]:
                    cnt += 1
                    break
    if cnt == 1:
        shift(flag, 9)
    elif cnt == 2:
        shift(flag, 9)
        shift(flag, 9)

score = 0
for _ in range(n):
    t, y, x = map(int, input().split())
    putBlue(t, y, x)
    while True:
        if not remove1(1):
            break
        score += 1
    remove2(1)
    putRed(t, y, x)
    while True:
        if not remove1(0):
            break
        score += 1
    remove2(0)

print(score)
cnt = 0
for i in range(10):
    for j in range(10):
        if g[i][j]:
            cnt += 1
print(cnt)
