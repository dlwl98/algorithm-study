n, m, k, t = map(int, input().split())

g = [0] * (n + 2)
for _ in range(m):
    come, go = map(int, input().split())
    for a in range(come, go):
        g[a] += 1
        g[a] = min(t, g[a])

sections = []
tmp = g[1]
cnt = 1
for i in range(2, n + 1):
    if tmp != g[i]:
        sections.append([cnt, t - tmp])
        tmp = g[i]
        cnt = 0
    cnt += 1
sections.append([cnt, t - tmp])

dp = [[0] * (k + 1) for _ in range(len(sections))]

def dfs(idx, remain, prev):
    if idx == len(sections):
        return 0
    if dp[idx][remain]:
        return dp[idx][remain]

    time, cost = sections[idx]
    if prev >= cost:
        cost = 0

    result = 0
    if remain - cost >= 0:
        result = max(dfs(idx + 1, remain - cost, cost) + time, dfs(idx + 1, remain, 0))
    else:
        result = dfs(idx + 1, remain, 0)

    dp[idx][remain] = result
    return result

print(dfs(0, k, 0))
