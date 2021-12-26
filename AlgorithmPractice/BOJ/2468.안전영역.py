import sys
from collections import deque

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, rain):
    queue = deque()
    queue.append([r, c])
    visited[r][c] = 1

    while queue:
        start_r, start_c = queue.popleft()

        for i in range(4):
            nr = start_r + dr[i]
            nc = start_c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if field[nr][nc] >= rain and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    queue.append([nr, nc])


N = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

field_max = 0
for i in range(N):
    for j in range(N):
        if field[i][j] > field_max:
            field_max = field[i][j]


max_safe = 0
for rain in range(1, field_max+1): # 1부터 가장 높은 높이까지
    visited = [[0] * N for _ in range(N)] # 한번 순회한 후 초기화해야 함
    cnt = 0  # 안전지역의 개수(한 번 순회하면 초기화)
    for i in range(N):
        for j in range(N):
            if field[i][j] >= rain and visited[i][j] == 0: # 물보다 높이가 높을 때 bfs
                bfs(i, j, rain)
                cnt += 1
    if max_safe < cnt:
        max_safe = cnt
print(max_safe)

# 지형이 rain보다 높아야 안 잠기는 것이 아닌가? 왜 field[i][j] >= rain이여야 답인거지???