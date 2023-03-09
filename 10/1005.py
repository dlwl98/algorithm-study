from sys import stdin

t = int(stdin.readline())

def solution():
    n, k = map(int, stdin.readline().split())
    b = [0] + list(map(int, stdin.readline().split()))
    g = [set() for _ in range(n + 1)]
    for _ in range(k):
        x, y = map(int, stdin.readline().split())
        if x not in g[y]:
            g[y].add(x)
    target = int(stdin.readline())
    dp = [-1] * (n + 1)

    def dfs(i):
        if dp[i] != -1:
            return dp[i]

        tmp = 0
        for sub in g[i]:
            tmp = max(tmp, dfs(sub))

        dp[i] = tmp + b[i]
        return dp[i]

    print(dfs(target))

for _ in range(t):
    solution()
