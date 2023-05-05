from sys import stdin

n, m = map(int, stdin.readline().split())
g = [[0] * (n + 1)] + [[0] + list(map(int, stdin.readline().split())) for _ in range(n)]
tree = [[0] * (n + 1) for _ in range(n + 1)]

def update(i, j, diff):
    while i <= n:
        tmp = j
        while tmp <= n:
            tree[i][tmp] += diff
            tmp += tmp & -tmp
        i += i & -i

def whole_sum(i, j):
    result = 0
    while i > 0:
        tmp = j
        while tmp > 0:
            result += tree[i][tmp]
            tmp -= tmp & -tmp
        i -= i & -i
    return result

def local_sum(x1, y1, x2, y2):
    return whole_sum(x2, y2) - whole_sum(x2, y1 - 1) - whole_sum(x1 - 1, y2) + whole_sum(x1 - 1, y1 - 1)

for i in range(1, n+1):
    for j in range(1, n+1):
        update(i, j, g[i][j])

for _ in range(m):
    arr = list(map(int, stdin.readline().split()))
    if arr[0] == 0:
        w, x, y, c = arr
        diff = c - g[x][y]
        g[x][y] = c
        update(x, y, diff)
    if arr[0] == 1:
        w, x1, y1, x2, y2 = arr
        print(local_sum(x1, y1, x2, y2))
