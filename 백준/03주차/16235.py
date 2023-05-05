from sys import stdin
from collections import deque

N, M, K = map(int, stdin.readline().split())
A = [list(map(int, stdin.readline().split())) for _ in range(N)]
G = [[5] * N for _ in range(N)]
T = [[deque([]) for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, age = map(int, stdin.readline().split())
    T[x-1][y-1].append(age)
dy = (-1, 1, 0, 0, -1, -1, 1, 1)
dx = (0, 0, -1, 1, -1, 1, -1, 1)
cnt = M


def year():
    global cnt
    # 봄 여름
    for i in range(N):
        for j in range(N):
            tmp = len(T[i][j])
            for k in range(tmp):
                if T[i][j][k] <= G[i][j]:
                    G[i][j] -= T[i][j][k]
                    T[i][j][k] += 1
                else:
                    for _ in range(k, tmp):
                        cnt -= 1
                        G[i][j] += T[i][j].pop() // 2
                    break

    # 가을 겨울
    for i in range(N):
        for j in range(N):
            for tree in T[i][j]:
                if tree % 5 != 0:
                    continue
                for k in range(8):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if 0 <= ny < N and 0 <= nx < N:
                        cnt += 1
                        T[ny][nx].appendleft(1)
            G[i][j] += A[i][j]


def solution():
    for _ in range(K):
        year()
    print(cnt)


solution()
