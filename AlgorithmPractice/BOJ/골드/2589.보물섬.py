import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    queue = deque()
    queue.append([r, c])

    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1
    distance = [[0] * M for _ in range(N)]
    cnt = 1

    while queue:
        r, c, = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                if arr[nr][nc] == 'L':
                    visited[nr][nc] = 1
                    distance[nr][nc] = distance[r][c] + 1
                    queue.append([nr, nc])
                    cnt = max(cnt, distance[nr][nc])
    return cnt



N, M = map(int, input().split()) # N: 행, M: 열
arr = [list(input().strip()) for _ in range(N)]

ans = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            ans = max(ans, bfs(i, j))

print(ans)






