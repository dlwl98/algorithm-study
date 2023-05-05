import sys
sys.setrecursionlimit(10 ** 5)

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 0

def go(start, end):
    if dp[start][end] != -1:
        return dp[start][end]
    
    result = 10 ** 9
    for mid in range(start, end):
        tmp = go(start, mid) + go(mid + 1, end) + g[start][0] * g[mid][1] * g[end][1]
        result = min(result, tmp)
    
    dp[start][end] = result
    return result

print(go(0, n-1))
