import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(red_r, red_c, blue_r, blue_c):
    queue = deque()
    queue.append([red_r, red_c, blue_r, blue_c])
    visited = []
    visited.append([red_r, red_c, blue_r, blue_c])
    cnt = 0 # 기울인 횟수

    while queue:
        for _ in range(len(queue)):
            red_r, red_c, blue_r, blue_c = queue.popleft()
            # 기울인 횟수가 10을 넘을 때
            if cnt > 10:
                print(-1)
                return
            # 빨간공이 탈출했을 때
            if arr[red_r][red_c] == 'O':
                print(cnt)
                return

            for i in range(4):
                # 빨간공의 이동
                nrr, nrc = red_r, red_c
                while True:
                    nrr += dr[i]
                    nrc += dc[i]
                    # 빨간공이 벽을 만나면 한 칸 뒤로
                    if arr[nrr][nrc] == '#':
                        nrr -= dr[i]
                        nrc -= dc[i]
                        break
                    # 빨간공이 구멍에 도착
                    if arr[nrr][nrc] == 'O':
                        break
                # 파란공의 이동
                nbr, nbc = blue_r, blue_c
                while True:
                    nbr += dr[i]
                    nbc += dc[i]
                    # 파란공이 벽을 만나면 한 칸 뒤로
                    if arr[nbr][nbc] == '#':
                        nbr -= dr[i]
                        nbc -= dc[i]
                        break
                    # 파란공이 구멍에 도착
                    if arr[nbr][nbc] == 'O':
                        break
                # 파란공이 먼저 들어갔을 때
                if arr[nbr][nbc] == 'O':
                    continue
                # 빨간공과 파란공이 만날 때
                if nrr == nbr and nrc == nbc:
                    # 더 많이 이동한 구슬이 더 늦게 이동한 구슬이므로 늦게 이동한 구슬 한칸 뒤로 이동
                    if abs(nrr - red_r) + abs(nrc - red_c) > abs(nbr - blue_r) + abs(nbc - blue_c):
                        nrr -= dr[i]
                        nrc -= dc[i]
                    else:
                        nbr -= dr[i]
                        nbc -= dc[i]
                if [nrr, nrc, nbr, nbc] not in visited:
                    queue.append([nrr, nrc, nbr, nbc])
                    visited.append([nrr, nrc, nbr, nbc])
        cnt += 1
    print(-1)

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            red_r, red_c = i, j # 빨간공의 좌표
        elif arr[i][j] == 'B':
            blue_r, blue_c = i, j # 파란공의 좌표

bfs(red_r, red_c, blue_r, blue_c)
