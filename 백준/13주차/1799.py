import heapq

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

def check(y, x):
    arr = set()
    for k in range(n):
        for dy, dx in ((-k, -k), (k, -k), (-k, k), (k, k)):
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < n and g[ny][nx]:
                arr.add((ny, nx))
    return arr

def change(arr, val):
    for y, x in arr:
        g[y][x] = val

result = 0
def dfs(cnt, flag):
    global result
    result = max(result, cnt)

    pq = []
    for i in range(n):
        for j in range(i % 2 if flag else (i+1) % 2, n, 2):
            if g[i][j]:
                arr = check(i, j)
                heapq.heappush(pq, (len(arr), i, j))

    if cnt + len(pq) <= result:
        return

    if not pq:
        return

    cost, y, x = heapq.heappop(pq)
    arr = check(y, x)
    change(arr, 0)
    dfs(cnt + 1, flag)
    change(arr, 1)
    while True:
        if not pq:
            return
        tmp, y, x = heapq.heappop(pq)
        if cost == tmp:
            arr = check(y, x)
            change(arr, 0)
            dfs(cnt + 1, flag)
            change(arr, 1)
        else:
            return

dfs(0, 1)
a = result
result = 0
dfs(0, 0)
b = result
print(a + b)
