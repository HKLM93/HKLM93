import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 빙하의 개수를 세줌
def counting(r, c):
    queue = deque()
    queue.append([r, c])
    visited[r][c] = 1

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] != 0 and visited[nr][nc] == 0:
                    queue.append([nr, nc])
                    visited[nr][nc] = 1

# 빙하가 녹음
def melting(r, c):

    zero_cnt = 0

    for idx in range(4):
        nr = r + dr[idx]
        nc = c + dc[idx]

        if arr_copy[nr][nc] == 0:
            zero_cnt += 1

    arr[r][c] = arr_copy[r][c] - zero_cnt
    if arr[r][c] < 0:
        arr[r][c] = 0


N, M = map(int, input().split()) # N: 행의 개수, M: 열의 개수
arr = [list(map(int, input().split())) for _ in range(N)]
arr_copy = deepcopy(arr)
time = 1 # 시간

while True:
    cnt = 0  # 빙하의 개수
    flag = True  # 빙하가 분리되지 않은 경우를 체크하기 위함

    # 빙하 녹기
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                melting(i, j)

    arr_copy = deepcopy(arr) # 빙하 갱신
    visited = [[0] * M for _ in range(N)]

    # 빙하 개수 세기
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and visited[i][j] == 0:
                counting(i, j)
                cnt += 1

    # 빙하의 분리 여부 확인
    for i in range(1, N-1):
        for j in range(1, M-1):
            if arr[i][j] != 0:
                flag = False
    if flag:
        print(0)
        break
    if cnt >= 2:
        print(time)
        break
    time += 1



