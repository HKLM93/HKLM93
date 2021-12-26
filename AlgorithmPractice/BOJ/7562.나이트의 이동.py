import sys
from collections import deque
input = sys.stdin.readline

# 나이트의 시작 위치를 기준으로도착하는 위치의 행, 열
dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

# 나이트의 이동
def knight(r, c):
    queue = deque()
    queue.append([r, c])
    chess[r][c] = 1

    while queue:
        r, c = queue.popleft()

        if r == next_p[0] and c == next_p[1]:
            return chess[next_p[0]][next_p[1]] -1 # 시작할 때 1을 주었기 때문에 1을 빼준다.

        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if chess[nr][nc] == 0:
                queue.append([nr, nc])
                chess[nr][nc] = chess[r][c] + 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    chess = [[0] * N for _ in range(N)]

    curr_p = list(map(int, input().split()))
    next_p = list(map(int, input().split()))

    print(knight(curr_p[0], curr_p[1]))



