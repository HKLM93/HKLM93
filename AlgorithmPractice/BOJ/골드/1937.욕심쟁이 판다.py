import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

######################################
# dp 활용
def dfs(r, c):
    if visited[r][c]:
        return visited[r][c]
    visited[r][c] = 1


    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N:
            if forest[nr][nc] > forest[r][c]:
                visited[r][c] = max(visited[r][c], dfs(nr, nc)+1)
    return visited[r][c]


N = int(input()) # 대나무 숲의 크기
forest = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)] # dp를 사용

ans = 1

for i in range(N):
    for j in range(N):
        ans = max(ans, dfs(i, j))

print(ans)

##########################################
# dfs 활용 - 시간 초과

def dfs(r, c, cnt):
    global ans

    if ans < cnt:
        ans = cnt
        return cnt


    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N:
            if forest[nr][nc] > forest[r][c]:
                visited[nr][nc] = 1
                dfs(nr, nc, cnt+1)
                visited[nr][nc] = 0


N = int(input()) # 대나무 숲의 크기
forest = [list(map(int, input().split())) for _ in range(N)]

ans = 1

for i in range(N):
    for j in range(N):
        visited = [[0] * N for _ in range(N)]
        visited[i][j] = 1
        dfs(i, j, 1)
print(ans)
