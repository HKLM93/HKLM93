import sys
from collections import deque
input = sys.stdin.readline

# 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
d = 1

def change(d, c):
    # 왼쪽 회전
    if c == 'L':
        d = (d-1) % 4
    # 오른쪽 회전
    else:
        d = (d+1) % 4
    return d

def move(r, c, time):  # 뱀 위치(r, c), 뱀의 길이, 게임 시간
    global d
    visited = deque()
    visited.append([r, c]) # 방문 위치 = 뱀의 위치
    arr[r][c] = 1

    while True:
        r = r + dr[d]
        c = c + dc[d]

        if 0 <= r < N and 0 <= c < N and arr[r][c] != 1: # 뱀이 보드 안에서 움직이고 자기 몸에 안 부딪혔을 때
            # 사과가 없으면
            if arr[r][c] != 2:
                tmp_r, tmp_c = visited.popleft()
                arr[tmp_r][tmp_c] = 0 # 꼬리 제거
            arr[r][c] = 1
            visited.append([r, c])
            if time in rotation.keys():
                d = change(d, rotation[time])
            time += 1
        # 본인 몸에 부딪히거나, 벽에 부딪힌 경우
        else:
            return time

N = int(input()) # N: 보드의 크기
K = int(input()) # K: 사과의 개수

arr = [[0] * N for _ in range(N)]

# apple = [] # 사과의 위치를 담을 리스트
for _ in range(K):
    apple_r, apple_c = map(int, input().split())
    arr[apple_r-1][apple_c-1] = 2 # 사과는 2로 표시
    # apple.append([apple_r, apple_c])
print(arr)

L = int(input()) # L: 뱀의 방향 변환 횟수

rotation = {}# 뱀이 회전 하는 시간과 회전방향을 담을 리스트
for _ in range(L):
    seconds, direction = input().split() # seconds: 게임 시작 후 뱀이 회전하는 시간, direction: 뱀이 회전하는 방향
    seconds = int(seconds)
    rotation[seconds] = direction

print(rotation)

print(move(0, 0, 1))