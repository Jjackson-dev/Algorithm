from collections import deque

n, m = map(int, input().split(' '))
graph = []

for line in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(row, col):
    queue = deque([(row, col)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>n-1 or ny<0 or ny>m-1:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))
