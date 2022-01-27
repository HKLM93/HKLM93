import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = 1
    cnt = 0

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                if arr[nr][nc] == 0:
                    visited[nr][nc] = 1
                    # 가장자리 체크를 위해 치즈가 아닌 부분만 넣는다
                    queue.append([nr, nc])
                elif arr[nr][nc] == 1:
                    arr[nr][nc] = 0
                    visited[nr][nc] = 1
                    cnt += 1
    ans.append(cnt)
    return cnt

N, M = map(int, input().split()) # N: 세로길이, M: 가로길이
arr = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
ans = []
time = 0

while True:
    time += 1
    visited = [[0] * M for _ in range(N)]
    cnt = bfs()

    if cnt == 0:
        break

print(time - 1)
print(ans[-2])