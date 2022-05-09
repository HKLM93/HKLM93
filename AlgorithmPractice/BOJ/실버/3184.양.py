from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    global total_sheep, total_wolf
    queue = deque()
    queue.append([r, c])
    sheep, wolf = 0, 0

    if arr[r][c] == "o":
        sheep += 1
    elif arr[r][c] == "v":
        wolf += 1

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < R and 0 <= nc < C and visit[nr][nc] == 0 and arr[nr][nc] != "#":
                if arr[nr][nc] == "o":
                    sheep += 1
                if arr[nr][nc] == "v":
                    wolf += 1

                visit[nr][nc] = 1
                queue.append([nr, nc])

    if sheep and wolf:
        if sheep > wolf:
            total_wolf -= wolf
        else:
            total_sheep -= sheep

R, C = map(int, input().split())
arr = []
visit = [[0] * C for i in range(R)]
total_sheep, total_wolf = 0, 0

for i in range(R):
    a = list(input().strip())
    for j in range(C):
        if a[j] == "o":
            total_sheep += 1
        if a[j] == "v":
            total_wolf += 1
    arr.append(a)
for i in range(R):
    for j in range(C):
        if (arr[i][j] == "o" or arr[i][j] == "v") and visit[i][j] == 0:
            visit[i][j] = 1
            bfs(i, j)
print(total_sheep, total_wolf)