import sys

tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())

    edges = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append([s, e, t])
        edges.append([e, s, t])
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append([s, e, -t])
    
    dp = [10**9] * (n+1)
    def bf():
        for i in range(n):
            for s, e, t in edges:
                if dp[s] + t < dp[e]:
                    dp[e] = dp[s] + t
                    if i == n-1:
                        return True
        return False

    if bf():
        print("YES")
    else:
        print("NO")
