import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(virus_list):
    visited = [[-1] * N for _ in range(N)]
    virus = deque()

    for i in virus_list:
        virus.append(i)
        visited[i[0]][i[1]] = 0

    max_n = 0
    while virus:
        r, c = virus.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1 and arr[nr][nc] != 1:
                visited[nr][nc] = visited[r][c] + 1
                if arr[nr][nc] == 0:
                    max_n = max(max_n, visited[nr][nc])
                virus.append([nr, nc])

    cnt = list(sum(visited, []))

    if cnt.count(-1) == list(sum(arr, [])).count(1):
        ans.append(max_n)


N, M = map(int, input().split()) # N: 연구소의 크기, M: 바이러스의 개수
arr = [list(map(int, input().split())) for _ in range(N)]

queue = []

ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            queue.append([i, j])

q = list(combinations(queue, M))

for i in q:
    bfs(i)

if ans:
    print(min(ans))
else:
    print(-1)





