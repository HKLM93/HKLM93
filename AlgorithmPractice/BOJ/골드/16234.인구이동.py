import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def move(r, c):
    queue = deque()
    queue.append([r, c])
    tmp = [] # 연합을 이룰 나라들을 담음
    tmp.append([r, c])

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if L <= abs(arr[nr][nc] - arr[r][c]) <= R:
                    visited[nr][nc] = 1
                    queue.append([nr, nc])
                    tmp.append([nr, nc])
    return tmp

N, L, R = map(int, input().split()) # L:인구 차이의 최소값, R: 인구 차이의 최대값
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
day = 0

while True:
    visited = [[0] * N for _ in range(N)]
    isTrue = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                tmp = move(i, j)
                # 연합이 있으면 인구 이동 시키기
                if len(tmp) > 1:
                    isTrue = True
                    num = sum([arr[r][c] for r, c in tmp]) // len(tmp)
                    for r, c in tmp:
                        arr[r][c] = num
    # 연합이 없으면
    if not isTrue:
        break
    day += 1

print(day)
