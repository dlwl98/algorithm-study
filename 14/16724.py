import sys
from collections import deque
input = sys.stdin.readline

n, m= map(int, input().split())
g = [[0] * m for _ in range(n)]
d = ((-1, 0), (1, 0), (0, 1), (0, -1))
dic = dict()
dic['D'], dic['U'], dic['L'], dic['R'] = 1, 0, 3, 2
v = [[False] * m for _ in range(n)]
w = [[[] for _ in range(m)] for _ in range(n)]

for i in range(n):
	a = list(input().rstrip())
	for j in range(m):
		g[i][j] = dic[a[j]]

cnt = 1
for i in range(n):
	for j in range(m):
		if not v[i][j]:
			cnt += 1
			q = deque()
			q.append((i, j))
			ref = [cnt]
			w[i][j] = ref
			v[i][j] = True
			while q:
				y, x = q.popleft()
				dy, dx = d[g[y][x]]
				if 0 <= y + dy < n and 0 <= x + dx < m:
					if not v[y + dy][x + dx]:
						q.append((y + dy, x + dx))
						v[y + dy][x + dx] = True
						w[y + dy][x + dx] = ref
					elif w[i][j][0] != w[y + dy][x + dx][0]:
						w[i][j][0] = w[y + dy][x + dx][0]

s = set()
for i in range(n):
	for j in range(m):
		s.add(w[i][j][0])
print(len(s))
