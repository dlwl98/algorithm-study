import heapq

problem_num = 0

def solution(n):
    g = [list(map(int, input().split())) for _ in range(n)]
    dist = [[10 ** 9] * n for _ in range(n)]
    q = []
    dist[0][0] = g[0][0]
    heapq.heappush(q, (dist[0][0], 0, 0))

    while q:
        cost, y, x = heapq.heappop(q)
        if dist[y][x] < cost:
            continue
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < n and g[ny][nx] + cost < dist[ny][nx]:
                dist[ny][nx] = g[ny][nx] + cost
                heapq.heappush(q, (dist[ny][nx], ny, nx))

    print('Problem ' + str(problem_num) + ':', end=' ')
    print(dist[n-1][n-1])


while True:
    N = int(input())
    problem_num += 1
    if N == 0:
        break
    else:
        solution(N)
