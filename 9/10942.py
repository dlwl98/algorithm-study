from sys import stdin

N = int(input())
G = [0] + list(map(int, stdin.readline().split()))
M = int(input())
orders = [list(map(int, stdin.readline().split())) for _ in range(M)]


def solution():
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        tmp = 0
        while i - tmp > 0 and i + tmp <= N:
            if i == i-tmp:
                dp[i][i] = 1
            else:
                if G[i-tmp] == G[i+tmp]:
                    dp[i-tmp][i+tmp] = 1
                else:
                    break
            tmp += 1
        s, e = i, i + 1
        while s > 0 and e <= N:
            if G[s] == G[e]:
                dp[s][e] = 1
            else:
                break
            s -= 1
            e += 1

    for s, e in orders:
        print(dp[s][e])


solution()
