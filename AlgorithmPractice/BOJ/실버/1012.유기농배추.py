import sys

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(r, c):
    queue = [(r, c)]

    while queue:
        start_r, start_c = queue.pop(0)

        for i in range(4):
            nr = start_r + dr[i]
            nc = start_c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M: # 범위를 벗어나지 않도록
                continue

            if farm_arr[nr][nc] == 1:
                farm_arr[nr][nc] = 0 # BFS를 한 범위는 0으로 바꿔줌
                queue.append([nr, nc])

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split()) # M은 가로길이, N은 세로길이, K는 배추의 개수

    farm_arr = [[0]*M for _ in range(N)] # 배추 심은 땅

    for t in range(K):
        x, y = map(int, input().split())
        farm_arr[y][x] = 1 # 배추의 위치 표기

    cnt = 0 # 배추흰지렁이 개수

    for i in range(N): # 땅을 탐색
        for j in range(M):
            if farm_arr[i][j] == 1:
                BFS(i, j)
                farm_arr[i][j] = 0 # 시작 지점도 0으로 바꿔줌
                cnt += 1 # BFS를 했으니 배추흰지렁이를 추가함

    print(cnt)