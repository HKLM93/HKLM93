import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c, cnt): #cnt는 쓰레기의 개수
    queue = deque()
    queue.append([r,c])
    visited[r][c] = 1

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] == 1:
                queue.append([nr, nc])
                visited[nr][nc] = 1
                cnt += 1
    return cnt

N, M, K = map(int, input().split()) # N:통로의 세로 길이, M:통로의 가로 길이, K: 음식물 쓰레기의 개수
arr = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
ans = 0

for _ in range(K):
    r, c = map(int, input().split())
    food_r, food_c = r -1, c - 1
    arr[food_r][food_c] = 1 # 음식물을 통로에 놓음

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            result = bfs(i, j, 1)
            ans = max(ans, result)
print(ans)





