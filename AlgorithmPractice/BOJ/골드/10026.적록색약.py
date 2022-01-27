import sys
from collections import deque
input = sys.stdin.readline


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    queue = deque()
    queue.append([r, c])
    visited[r][c] = 1

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if area[nr][nc] == area[r][c] and visited[nr][nc] == 0:
                queue.append([nr, nc])
                visited[nr][nc] = 1


N = int(input())
area = [list(input().strip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

cnt_1 = 0

# 일반적인 사람
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt_1 += 1

# 적록색약은 R과 G를 같게 본다
for i in range(N):
    for j in range(N):
        if area[i][j] == 'R':
            area[i][j] = 'G'
# 방문 그래프 초기화
visited = [[0] * N for _ in range(N)]

# 적록색약의 경우
cnt_2 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt_2 += 1

print(cnt_1, cnt_2)