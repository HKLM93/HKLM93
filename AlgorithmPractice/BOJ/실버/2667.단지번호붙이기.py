import sys

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(r, c):
    queue = []
    queue.append((r, c))
    visited[r][c] = 1
    count = 1 # 단지 개수

    while queue:
        start_r, start_c = queue.pop(0)

        for i in range(4):
            nr = start_r + dr[i]
            nc = start_c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N: # 범위를 벗어나지 않도록
                continue

            if arr[nr][nc] == 1 and visited[nr][nc] == 0:
                queue.append((nr, nc))
                visited[nr][nc] = 1
                count += 1
    return count

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

visited = [[0]*N for _ in range(N)]

cnt = [] # 단지 번호
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt.append(BFS(i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])



