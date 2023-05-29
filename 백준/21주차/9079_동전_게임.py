from itertools import combinations

t = int(input())

def check(g):
    for i in range(3):
        for j in range(3):
            if g[0][0] != g[i][j]:
                return False
    return True

def change(i, g):
    if 0 <= i <=2:
        for j in range(3):
            if g[i][j] == 'H':
                g[i][j] = 'T'
            else:
                g[i][j] = 'H'
    if 3 <= i <= 5:
        for j in range(3):
            if g[j][i-3] == 'H':
                g[j][i-3] = 'T'
            else:
                g[j][i-3] = 'H'
    if i == 6:
        if g[0][0] == 'H':
            g[0][0] = 'T'
        else:
            g[0][0] = 'H'
        if g[1][1] == 'H':
            g[1][1] = 'T'
        else:
            g[1][1] = 'H'
        if g[2][2] == 'H':
            g[2][2] = 'T'
        else:
            g[2][2] = 'H'

    if i == 7:
        if g[0][2] == 'H':
            g[0][2] = 'T'
        else:
            g[0][2] = 'H'
        if g[1][1] == 'H':
            g[1][1] = 'T'
        else:
            g[1][1] = 'H'
        if g[2][0] == 'H':
            g[2][0] = 'T'
        else:
            g[2][0] = 'H'

def solution():
    g = [list(input().split()) for _ in range(3)]
    if check(g):
        print(0)
        return
    for i in range(1, 9):
        for com in combinations(range(8), i):
            origin = [[0] * 3 for _ in range(3)]
            for a in range(3):
                for b in range(3):
                    origin[a][b] = g[a][b]

            for j in com:
                change(j, g)

            if check(g):
                print(len(com))
                return
            else:
                for a in range(3):
                    for b in range(3):
                        g[a][b] = origin[a][b]
    print(-1)

for _ in range(t):
    solution()
