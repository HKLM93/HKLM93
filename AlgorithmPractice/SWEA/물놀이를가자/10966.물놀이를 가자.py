import sys
sys.stdin = open('sample_input.txt', 'r')
from collections import deque

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 1. 선형큐 활용
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split()) # N은 세로크기, M은 가로크기
#
#     arr = [input() for _ in range(N)]
#
#     dist = [[987654321] * M for _ in range(N)] # 방문체크 겸 거리 체크
#
#     Q = [0] * (N*M)
#     front = -1
#     rear = -1
#
#
#     # 시작점인 물을 몽땅 담기
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 'W':
#                 rear += 1
#                 Q[rear] = (i, j)
#                 dist[i][j] = 0
#
#     while front != rear:
#         front += 1
#         r, c = Q[front]
#
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#
#             if nr < 0or nr >= N or nc <0 or nc >=M:
#                 continue
#
#             if arr[nr][nc] == 'L' and dist[nr][nc] == 987654321:
#                 dist[nr][nc] = dist[r][c] + 1
#                 rear += 1
#                 Q[rear] = (nr, nc)
#     ans = 0
#
#     for i in dist:
#         for j in i:
#             ans += j
#
#     print('#{} {}'.format(tc, ans))

####################################################
#2. deque 활용

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N은 세로크기, M은 가로크기

    arr = [input() for _ in range(N)]

    dist = [[987654321] * M for _ in range(N)]  # 방문체크 겸 거리 체크

    queue = deque()

    # 시작점인 물을 몽땅 담기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                queue.append([i, j])
                dist[i][j] = 0

    # W에서 L에 해당하는 모든 부분을 방문하도록 함
    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if arr[nr][nc] == 'L' and dist[nr][nc] == 987654321:
                dist[nr][nc] = dist[r][c] + 1
                queue.append([nr, nc])

    ans = 0

    for i in dist:
        for j in i:
            ans += j

    print('#{} {}'.format(tc, ans))


