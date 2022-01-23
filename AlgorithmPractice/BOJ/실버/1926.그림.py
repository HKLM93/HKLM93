import sys
# sys.setrecursionlimit(10**9)
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
#######################
# dfs는 메모리 초과가 나온다
# def dfs(r, c):
#     global cnt
#     cnt += 1
#     visited[r][c] = 1
#
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#
#         if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0 and arr[nr][nc] == 1:
#             visited[nr][nc] = 1
#             dfs(nr, nc)
#
#
# n, m = map(int, input().split()) # n:도화지의 세로 크기, m: 도화지의 가로 크기
# arr = [list(map(int, input().split())) for _ in range(n)]
#
# visited = [[0] * m for _ in range(n)]
# result = []
# for i in range(n):
#     for j in range(m):
#         if arr[i][j] == 1 and visited[i][j] == 0:
#             cnt = 0
#             dfs(i, j)
#             result.append(cnt)
#
# if len(result) == 0:
#     print(len(result))
#     print(0)
# else:
#     print(len(result))
#     print(max(result))

###########################################

def bfs(r, c):
    cnt = 1
    queue = deque()
    queue.append([r, c])
    visited[r][c] = 1

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if graph[nr][nc] == 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    queue.append([nr, nc])
                    cnt += 1  # update each_cnt
    return cnt  # end each_cnt


n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]

result, max_count = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            result += 1
            max_count = max(max_count, bfs(i, j))

print(result)
print(max_count)

