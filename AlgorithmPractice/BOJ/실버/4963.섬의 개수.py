import sys
from collections import deque

# 북, 북동, 동, 동남, 남, 남서, 서, 북서
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(r, c):
    queue = deque()
    queue.append([r, c])

    while queue:
        start_r, start_c = queue.popleft()

        for i in range(8):
            nr = start_r + dr[i]
            nc = start_c + dc[i]

            if nr < 0 or nr >= h or nc < 0 or nc >= w:
                continue

            if map_arr[nr][nc] == 1:
                map_arr[nr][nc] = 0
                queue.append([nr, nc])

while True:
    w, h = map(int, sys.stdin.readline().split()) # w는 지도의 너비, h는 지도의 높이 / 0 <= w, h <= 50
    if w == 0 and h == 0: # 마지막 줄에 0 0 이 출력 됨으로 반복문 종료
        break

    cnt = 0 # 섬의 개수
    map_arr = []
    for i in range(h):
        map_arr.append(list(map(int, sys.stdin.readline().split())))

    for i in range(h):
        for j in range(w):
            if map_arr[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)