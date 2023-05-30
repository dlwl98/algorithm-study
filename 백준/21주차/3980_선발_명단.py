import sys
sys.setrecursionlimit(10**5)

c = int(input())
for _ in range(c):
    g = [list(map(int, input().split())) for _ in range(11)]
    stats = [[] for _ in range(11)]
    for i in range(11):
        for j in range(11):
            if g[i][j] > 0:
                stats[i].append([g[i][j], j])
    v = [False] * 11
    result = 0

    def go(i, acc):
        global result
        if i >= 11:
            result = max(result, acc)
            return
        for stat, j in stats[i]:
            if not v[j]:
                v[j] = True
                go(i+1, acc + stat)
                v[j] = False

    go(0, 0)
    print(result)
