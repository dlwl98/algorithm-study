import copy
import sys
sys.setrecursionlimit(10**5)

directions = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
g = [[[0, 0] for _ in range(4)] for _ in range(4)]
fishes = [[0, 0] for _ in range(17)]

for i in range(4):
    arr = list(map(int, input().split()))
    for j in range(4):
        g[i][j][0] = arr[j*2]
        g[i][j][1] = arr[j*2 + 1] - 1
        fishes[arr[j*2]] = [i, j]

def inRange(y, x):
    return 0 <= y < 4 and 0 <= x < 4

def check(y, x, g, fishes):
    fish, d = g[y][x]
    ny = y + directions[d][0]
    nx = x + directions[d][1]
    if inRange(ny, nx):
        if fishes[0] == [ny, nx]:
            return False
        else:
            return True
    else:
        return False

def move(y, x, g, fishes):
    while not check(y, x, g, fishes):
        g[y][x][1] = (g[y][x][1] + 1) % 8
    fish, d = g[y][x]
    ny = y + directions[d][0]
    nx = x + directions[d][1]
    nfish, nd = g[ny][nx]
    if fishes[fish] != [-1, -1]:
        fishes[fish] = [ny, nx]
    if fishes[nfish] != [-1, -1]:
        fishes[nfish] = [y, x]
    g[ny][nx] = [fish, d]
    g[y][x] = [nfish, nd]

result = 0
def eat(acc, g, fishes, y, x):
    global result
    result = max(result, acc)
    cg = copy.deepcopy(g)
    cfishes = copy.deepcopy(fishes)

    cfishes[0] = [y, x]
    cfishes[cg[y][x][0]] = [-1, -1]

    for i in range(1, 17):
        if cfishes[i][0] != -1:
            move(cfishes[i][0], cfishes[i][1], cg, cfishes)

    for i in range(1, 4):
        ny = y + directions[cg[y][x][1]][0] * i
        nx = x + directions[cg[y][x][1]][1] * i
        if inRange(ny, nx) and cfishes[cg[ny][nx][0]][0] != -1:
            eat(acc + cg[ny][nx][0], cg, cfishes, ny, nx)

eat(g[0][0][0], g, fishes, 0, 0)
print(result)
