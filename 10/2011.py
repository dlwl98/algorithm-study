import sys
sys.setrecursionlimit(10**5)

def solution():
    target = input()
    n = len(target)
    dp = [-1] * (n + 1)

    def check(s):
        if len(s) == 1 and 1 <= int(s) <= 9:
            return True
        if len(s) == 2 and 10 <= int(s) <= 26:
            return True
        return False

    def dfs(s):
        if dp[len(s)] != -1:
            return dp[len(s)]

        tmp = 0
        if check(s):
            tmp += 1
        if len(s) > 1 and check(s[0]):
            tmp += dfs(s[1:])
        if len(s) > 2 and check(s[0] + s[1]):
            tmp += dfs(s[2:])

        tmp %= 1000000
        dp[len(s)] = tmp
        return tmp

    print(dfs(target))

solution()
