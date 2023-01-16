from sys import stdin

N, M = map(int, stdin.readline().split())
g = [[0] * 505 for _ in range(505)]
for n in range(N):
    inputs = list(map(int, stdin.readline().split()))
    for m in range(len(inputs)):
        g[n][m] = inputs[m]


def solution():
    max_val = 0
    for i in range(N):
        for j in range(M):
            max_val = max(max_val, g[i][j] + g[i][j + 1] + g[i][j + 2] + g[i][j + 3])
            max_val = max(max_val, g[i][j] + g[i + 1][j] + g[i + 2][j] + g[i + 3][j])
            max_val = max(max_val, g[i][j] + g[i][j + 1] + g[i + 1][j] + g[i + 1][j + 1])
            max_val = max(max_val, g[i][j] + g[i + 1][j] + g[i + 2][j] + g[i + 2][j + 1])
            max_val = max(max_val, g[i][j] + g[i][j + 1] + g[i][j + 2] + g[i + 1][j])
            max_val = max(max_val, g[i][j] + g[i][j + 1] + g[i + 1][j + 1] + g[i + 2][j + 1])
            max_val = max(max_val, g[i][j + 2] + g[i + 1][j] + g[i + 1][j + 1] + g[i + 1][j + 2])
            max_val = max(max_val, g[i][j + 1] + g[i + 1][j + 1] + g[i + 2][j] + g[i + 2][j + 1])
            max_val = max(max_val, g[i][j] + g[i][j + 1] + g[i][j + 2] + g[i + 1][j + 2])
            max_val = max(max_val, g[i][j] + g[i][j + 1] + g[i + 1][j] + g[i + 2][j])
            max_val = max(max_val, g[i][j] + g[i + 1][j] + g[i + 1][j + 1] + g[i + 1][j + 2])
            max_val = max(max_val, g[i][j] + g[i + 1][j] + g[i + 1][j + 1] + g[i + 2][j + 1])
            max_val = max(max_val, g[i][j + 1] + g[i][j + 2] + g[i + 1][j] + g[i + 1][j + 1])
            max_val = max(max_val, g[i][j + 1] + g[i + 1][j] + g[i + 1][j + 1] + g[i + 2][j])
            max_val = max(max_val, g[i][j] + g[i][j + 1] + g[i + 1][j + 1] + g[i + 1][j + 2])
            max_val = max(max_val, g[i][j + 1] + g[i + 1][j] + g[i + 1][j + 1] + g[i + 1][j + 2])
            max_val = max(max_val, g[i][j] + g[i + 1][j] + g[i + 1][j + 1] + g[i + 2][j])
            max_val = max(max_val, g[i][j] + g[i][j + 1] + g[i][j + 2] + g[i + 1][j + 1])
            max_val = max(max_val, g[i][j + 1] + g[i + 1][j] + g[i + 1][j + 1] + g[i + 2][j + 1])
    print(max_val)


solution()

# 아래는 dfs 풀이..
# import sys
# input=sys.stdin.readline
#
# dx=[0,1,0,-1]
# dy=[1,0,-1,0]
#
# def dfs(x,y,L,res):
#     global answer
#     if answer >= res + MAX*(4-L):
#         return
#     if L==4:
#         answer = max(answer, res)
#         return
#     for i in range(4):
#         nx=x+dx[i]
#         ny=y+dy[i]
#         if 0 <= nx < m and 0 <= ny < n and visit[ny][nx]==0:
#             if L==2:
#                 visit[ny][nx]=1
#                 dfs(x,y,L+1,res+board[ny][nx])
#                 visit[ny][nx]=0
#             visit[ny][nx]=1
#             dfs(nx,ny,L+1,res+board[ny][nx])
#             visit[ny][nx]=0
#
# if __name__ == "__main__":
#     n,m=map(int,input().split())
#     board=[list(map(int,input().split())) for _ in range(n)]
#     answer,MAX = 0,max(map(max,board))
#     visit=[[0]*m for _ in range(n)]
#
#     for i in range(n):
#         for j in range(m):
#             visit[i][j]=1
#             dfs(j,i,1,board[i][j])
#             visit[i][j]=0
#
#     print(answer)
