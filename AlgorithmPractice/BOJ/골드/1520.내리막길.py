import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 접근방법: 그냥 dfs는 시간초과가 난다. dp도 같이 사용해준다.

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):

    # 도착
    if r == M-1 and c == N-1:
        return 1

    if visited[r][c] != -1:
        return visited[r][c]

    visited[r][c] = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= M or nc < 0 or nc >= N:
            continue

        if field[nr][nc] < field[r][c]:
            visited[r][c] += dfs(nr, nc)

    return visited[r][c]

M, N = map(int, input().split()) # M은 세로(행), N은 가로(열)
field = [list(map(int, input().split())) for _ in range(M)]

visited = [[-1] * N for _ in range(M)]

print(dfs(0, 0))


