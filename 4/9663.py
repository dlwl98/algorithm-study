N = int(input())
G = [[0] * N for _ in range(N)]
row = [0] * N
result = 0


def check(depth):
    for i in range(depth):
        if row[depth] == row[i]:
            return False
        if abs(row[depth] - row[i]) == depth - i:
            return False
    return True


def dfs(depth):
    global result
    if depth == N:
        result += 1
        return
    for x in range(N):
        row[depth] = x
        if check(depth):
            dfs(depth + 1)


def solution():
    dfs(0)
    print(result)


solution()
