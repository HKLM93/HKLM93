import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    queue = deque()
    queue.append([r, c])
    field[r][c] = 1
    cnt = 0 # 영역의 크기

    while queue:
        r, c = queue.popleft()
        cnt += 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= M or nc < 0 or nc >= N:
                continue

            if field[nr][nc] == 0:
                queue.append([nr, nc])
                field[nr][nc] = 1
    area.append(cnt)


M, N, K = map(int, input().split()) # M: 행, N: 열, K: 직사각형의 개수

field = [[0] * N for _ in range(M)] # 모눈종이

ans = 0 # 영역의 개수
area = [] # 영역의 크기를 담을 리스트
for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    # 모눈종이에 사각형 집어 넣기
    for y in range(y1, y2):
        for x in range(x1, x2):
            field[y][x] = 2

for i in range(M):
    for j in range(N):
        if field[i][j] == 0:
            bfs(i, j)
            ans += 1

print(ans)
area.sort()
for i in area:
    print(i, end= ' ')

