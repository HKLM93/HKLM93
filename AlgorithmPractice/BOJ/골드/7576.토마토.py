import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(r, c):
    global queue

    while queue:
        start_r, start_c = queue.popleft()

        for i in range(4):
            nr = start_r + dr[i]
            nc = start_c + dc[i]

            if 0 > nr or nr >= N or nc < 0 or nc >= M:
                continue
            if box_arr[nr][nc] == 0:
                queue.append([nr, nc])
                box_arr[nr][nc] = box_arr[start_r][start_c] + 1


M, N = map(int, sys.stdin.readline().split())
box_arr = [list(map(int, input().split())) for _ in range(N)]


queue = deque()

for i in range(N):
    for j in range(M):
        if box_arr[i][j] == 1:
            queue.append([i,j])

BFS(i, j)

result = -2 # 임의의 최소값
check = False # 안 익은 토마토가 있으면 -1을 출력하기 위함

# 토마토 상태 확인
for i in box_arr:
    for j in i:
        if j == 0:
            check = True
        result = max(result, j)

if check == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)














