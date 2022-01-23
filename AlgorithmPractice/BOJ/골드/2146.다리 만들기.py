import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs1(r, c):
    global cnt
    queue = deque()
    queue.append([r, c])
    visited[r][c] = 1
    arr[r][c] = cnt

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                arr[nr][nc] = cnt
                queue.append([nr, nc])

def bfs2(num): # num은 섬의 번호
    global ans
    queue = deque()
    dist = [[-1] * N for _ in range(N)]

    # 같은 섬들을 거리 리스트에 넣어줌
    for i in range(N):
        for j in range(N):
            if arr[i][j] == num:
                queue.append([i, j])
                dist[i][j] = 0

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                # 다른 섬을 만났을 때
                if arr[nr][nc] > 0 and arr[nr][nc] != num:
                    ans = min(ans, dist[r][c])
                    return

                if arr[nr][nc] == 0 and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append([nr, nc])


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt = 1 # 섬 번호
ans = 987654321

# 섬을 번호로 구별
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            bfs1(i, j)
            cnt += 1

# 다리 연결
for i in range(1, cnt):
    bfs2(i)

print(ans)
