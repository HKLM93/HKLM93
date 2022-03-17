import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, cnt):
    global ans, room_num

    queue = deque()
    queue.append([r, c])

    while queue:
        start_r, start_c = queue.popleft()
        # 4방향 탐색
        for i in range(4):
            nr = start_r + dr[i]
            nc = start_c + dc[i]

            # 범위 설정
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            # 현재 값보다 1이 크면 이동
            if room[nr][nc] == room[start_r][start_c] + 1:
                queue.append([nr, nc])
                cnt += 1 # 방을 갈 수 있으면 개수 1추가

    # 방의 개수가 최대인 방
    if cnt > ans:
        ans = cnt
        room_num = room[r][c]
    # 방의 개수가 최대인 방이 여럿인 경우
    elif cnt == ans:
        # 그 중에서 적힌 수가 가장 작은 것
        if room[r][c] < room_num:
            room_num = room[r][c]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    ans = 0 # 시작하는 방도 세기 때문에 그거보다 작은 값을 초기값으로 설정
    room_num = 987654321 # 방의 최소값을 구하기 위한 초기값

    for i in range(N):
        for j in range(N):
            bfs(i, j, 1)

    print('#{} {} {}'.format(tc, room_num, ans))


####################################################################
# 추가 풀이방법
# 1차원 리스트로 연속된 1의 개수 체크 방법

# 상하좌우
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     room = [list(map(int, input().split())) for _ in range(N)]
#
#     visited = [0] * (N*N+1) # 해당방과 다음방이 연결되어 있는지 확인
#
#     for i in range(N):
#         for j in range(N):
#             # 각방을 한 번씩 방문
#             for k in range(4):
#                 nr = i + dr[k]
#                 nc = j + dc[k]
#
#                 if 0 <= nr < N and 0 <= nc < N and room[i][j] + 1 == room[nr][nc]:
#                     visited[room[i][j]] = 1
#
#     cnt = 0 # 1의 개수를 세기 위함
#     st_num = 0 # 시작 방의 번호
#     max_cnt = 0 # 방의 개수를 확인
#
#     for i in range(N*N, -1, -1):  # 1번 방부터 시작할 수 있어서 0번 인덱스까지 찾기
#         if visited[i] == 1:
#             cnt += 1 # 방이 연결되어 있음
#         else:
#             if max_cnt <= cnt:
#                 max_cnt = cnt
#                 st_num = i + 1 # 한 칸 더 이동
#             cnt = 0 # 초기화
#
#     print('#{} {} {}'.format(tc, st_num, max_cnt+1))
#

##################################################################
# 2. 위치와 거리를 이용
# for tc in range(1, int(input())+1):
#     N = int(input())
#     room = []
#     room_pos = [0] * (N*N+1)
#     room_dist = [1] * (N*N+1)
#
#     # 입력 받으면서 위치정보를 저장
#     for i in range(N):
#         # tmp = list(map(int, input().split()))
#         # for j in range(N):
#         #     room_pos[tmp[j]] = (i, j)
#         # 또는
#         room.append(list(map(int, input().split())))
#         for j in range(N):
#             room_pos[room[i][j]] = (i, j)
#
#     # 거리정보를 저장
#     for i in range(2, N*N+1):
#         for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             # 1차원리스트 안에 튜플을 넣어서 2차원 리스트처럼 접근이 가능
#             nr = room_pos[i][0] + dr
#             nc = room_pos[i][1] + dc
#
#             if 0 <= nr < N and 0 <= nc < N and room[nr][nc] == i-1: # i를 방번호로 쓰고 순회하는 중
#                 room_dist[i] = room_dist[i-1] + 1
#                 break
#
#     # 정답을 뽑아내자
#     st_num = 0
#     max_cnt = 0
#
#     for i in range(1, N*N+1):
#         if room_dist[i] > max_cnt:
#             st_num =i - max_cnt + 1
#             max_cnt = room_dist[i]
#
#     print('#{} {} {}'.format(tc, st_num, max_cnt))




