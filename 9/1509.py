from sys import stdin


def solution():
    g = '0' + stdin.readline().rstrip('\n')
    n = len(g) - 1
    pel = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        tmp = 0
        while i - tmp > 0 and i + tmp <= n:
            if i == i-tmp:
                pel[i][i] = 1
            else:
                if g[i-tmp] == g[i+tmp]:
                    pel[i-tmp][i+tmp] = 1
                else:
                    break
            tmp += 1
        s, e = i, i + 1
        while s > 0 and e <= n:
            if g[s] == g[e]:
                pel[s][e] = 1
            else:
                break
            s -= 1
            e += 1

    dp = [2500] * (n + 1)
    dp[0] = 0
    for end in range(1, n + 1):
        for start in range(1, end + 1):
            if pel[start][end]:
                dp[end] = min(dp[end], dp[start - 1] + 1)
            else:
                dp[end] = min(dp[end], dp[end - 1] + 1)
    print(dp[n])


solution()
