import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append([0, 0, 1])
    # 방문 체크 리스트를 3차원으로 만들어 벽을 부술 수 있는 횟수를 넣어줄 수 있도록 함
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][1] = 1

    while queue:
        r, c, wall = queue.popleft() # 좌표와 벽을 부술 수 있는 남은 횟수

        if r == (N-1) and c == (M-1):
            return visited[r][c][wall]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if arr[nr][nc] == 1 and wall == 1: # 벽을 한 개 부숨
                visited[nr][nc][0] = visited[r][c][1] + 1
                queue.append([nr, nc, 0]) # 횟수를 다 썼으니 -1 해줌

            elif arr[nr][nc] == 0 and visited[nr][nc][wall] == 0: # 빈 방이라면
                queue.append([nr, nc, wall])
                visited[nr][nc][wall] = visited[r][c][wall] + 1
    # 못찾으면
    return -1


N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

print(bfs())

# 완벽하게 이해를 못했다.... ㅠ

