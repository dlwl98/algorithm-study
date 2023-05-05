from sys import stdin
from collections import deque

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
R, C = map(int, stdin.readline().split())
G = [list(stdin.readline().rstrip('\n')) for _ in range(R)]
goose = []
v = [[False] * C for _ in range(R)]
wv = [[False] * C for _ in range(R)]
q = deque()
q_tmp = deque()
wq = deque()
wq_tmp = deque()


def check():
    while q:
        y, x = q.popleft()
        if G[y][x] == 'L' and goose != [y, x]:
            return True
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < R and 0 <= nx < C and not v[ny][nx]:
                v[ny][nx] = True
                if G[ny][nx] == 'X':
                    q_tmp.append([ny, nx])
                else:
                    q.append([ny, nx])
    return False


def melt():
    while wq:
        y, x = wq.popleft()
        if G[y][x] == 'X':
            G[y][x] = '.'
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < R and 0 <= nx < C and not wv[ny][nx]:
                wv[ny][nx] = True
                if G[ny][nx] == 'X':
                    wq_tmp.append([ny, nx])
                else:
                    wq.append([ny, nx])


def solution():
    global goose, q, q_tmp, wq, wq_tmp

    for i in range(R):
        for j in range(C):
            if G[i][j] == 'L':
                goose = [i, j]
                wq.append([i, j])
            if G[i][j] == '.':
                wv[i][j] = True
                wq.append([i, j])

    y, x = goose
    v[y][x] = True
    q.append([y, x])
    cnt = 0

    while True:
        melt()
        if check():
            print(cnt)
            break
        q = q_tmp
        wq = wq_tmp
        q_tmp = deque()
        wq_tmp = deque()
        cnt += 1


solution()
