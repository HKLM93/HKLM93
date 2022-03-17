import sys
import copy
from collections import deque

# 접근방법: 모든 경우의 벽을 세운 후에 bfs를 시행한다. 안전구역이 제일 많은 값을 답으로 출력

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    global ans
    virus = copy.deepcopy(lab_arr) # 벽을 3개 세운 후 바이러스가 퍼진 경우를 통해 답을 얻기 위함
    for i in range(N):
        for j in range(M):
            if virus[i][j] == 2:
                queue.append([i, j])

    while queue:
        start_r, start_c = queue.popleft()

        for i in range(4):
            nr = start_r + dr[i]
            nc = start_c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if virus[nr][nc] == 0:
                virus[nr][nc] = 2
                queue.append([nr, nc])

    safe_count = 0  # 안전구역의 개수
    for i in virus:
        safe_count += i.count(0)
    ans = max(ans, safe_count)

def select_wall(cnt): # cnt는 벽의 개수
    if cnt == 3: # 벽을 3개 다 세우면 bfs 실행
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if lab_arr[i][j] == 0:
                lab_arr[i][j] = 1
                select_wall(cnt+1) # 재귀를 통해서 벽을 3개 세움
                lab_arr[i][j] = 0 # 끝나면 초기화




N, M = map(int, sys.stdin.readline().split())
lab_arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
queue = deque()
ans = 0
select_wall(0)
print(ans)













