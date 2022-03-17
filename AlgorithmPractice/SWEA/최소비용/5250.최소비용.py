import sys
sys.stdin = open('sample_input.txt', 'r')

# 상하좌우
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# def dfs(r, c, distance, result): # result는 거리 + 내가 가는 길 중 가장 큰 높이
#     global ans
#     # 도착
#     if r == N-1 and c == N-1:
#         if ans > result:
#             ans = result
#             return
#     # 가지치기
#     if ans < result:
#         return
#
#     visited[r][c] = 1
#
#     for i in range(2):
#         nr = r + dr[i]
#         nc = c + dc[i]
#
#         if nr < 0 or nr >= N or nc < 0 or nc >= N:
#             continue
#
#         if visited[nr][nc] == 0:
#             visited[nr][nc] = 1
#             route.append(arr[nr][nc])
#             dfs(nr, nc, distance + 1, distance + 1 + max(route))
#             visited[nr][nc] = 0 # 방문 초기화
#             route.pop() # 갔던 길 없애기
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     visited = [[0]*N for _ in range(N)] # 중복 체크용
#     route = [arr[0][0]] # 가는 길을 담을 리스트
#     distance = 0 # 거리(기본 연료)
#     ans = 9987654321
#     result = distance + max(route) # 결국 기본 거리 + 가는 길에서 가장 높은 값을 더하면 된다.
#
#     dfs(0, 0, distance, result)
#
#
#     print('#{} {}'.format(tc, ans))
# dfs는 시간 초과 ㅠㅠㅠㅠ

#####################################################################################
# bfs

# 상하좌우
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# def bfs():
#     Q = [0] * 1000000
#     front = rear = -1
#
#     rear += 1
#     Q[rear] = (0, 0)
#     dist[0][0] = 0
#
#     while front != rear:
#         front += 1
#         r, c = Q[front]
#
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#
#             if 0 <= nr < N and 0 <= nc < N:
#                 if arr[nr][nc] > arr[r][c]:
#                     power = arr[nr][nc] - arr[r][c]
#                 else:
#                     power = 0
#
#                 if dist[nr][nc] > dist[r][c] + power +1:
#                     rear += 1
#                     Q[rear] = (nr, nc)
#                     dist[nr][nc] = dist[r][c] + power +1
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     dist = [[987654321] * N for _ in range(N)]
#
#     bfs()
#
#     print(dist[N-1][N-1])

####################################################################################
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 높이차이가 가중치라고 보면 된다.
def dijkstra():
    fuel = [[987654321] * N for _ in range(N)] # 연료 사용량
    fuel[0][0] = 0 # 시작값은 0

    queue = []
    queue.append((0,0))

    while queue:
        r, c = queue.pop(0)

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            height = 0 # 높이 차이
            if arr[nr][nc] > arr[r][c]: # 높이 차이가 나면
                height = arr[nr][nc] - arr[r][c]
            # 새롭게 갈 최단 거리가 현위치의 최단거리+높이차이+기본비용 보다 크면 갱신
            if fuel[nr][nc] > fuel[r][c] + height + 1:
                fuel[nr][nc] = fuel[r][c] + height + 1
                # 다음 좌표 집어 넣어줌
                queue.append((nr, nc))

    return fuel[N-1][N-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print('#{} {}'.format(tc, dijkstra()))