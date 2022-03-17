import sys
sys.stdin = open('sample_input.txt', 'r')
from collections import deque

# 우하좌상
dr = [0, 1,  0, -1]
dc = [1, 0, -1, 0]

# 터널 구조물
pipe = [
    # 없음
    [0, 0, 0, 0],
    # 상하좌우
    [1, 1, 1, 1],
    # 상하
    [0, 1, 0, 1],
    # 좌우
    [1, 0, 1, 0],
    # 상우
    [1, 0, 0, 1],
    # 하우
    [1, 1, 0, 0],
    # 하좌
    [0, 1, 1, 0],
    # 상좌
    [0, 0, 1, 1],
]

# 탈주범 위치 찾기
def bfs(r, c):
    global ans
    queue = deque()
    queue.append([r, c])
    visited[r][c] = 1

    while queue:
        start_r, start_c = queue.popleft()
        ans += 1

        if visited[start_r][start_c] >= L:
            continue

        for i in range(4):
            curr_p = tunnel[start_r][start_c]

            nr = start_r + dr[i]
            nc = start_c + dc[i]

            # 현재 바라보는 방향에 길이 없을 경우에 넘어감
            if pipe[curr_p][i] == 0:
                continue

            # 범위 설정
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            pn = tunnel[nr][nc] # 다음으로 연결된 파이프의 번호
            pd = (i+2) % 4 # 현재 파이프의 연결 상태

            # 터널이 존재하고 방문을 안 했고 파이프가 연결이 되어 있을 때
            if visited[nr][nc] == 0 and pipe[pn][pd] == 1:
                queue.append([nr, nc])
                visited[nr][nc] = visited[start_r][start_c] + 1


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split()) # N, M은 지도의 세로크기와 가로 크기/ R,C는 맨홀 위치의 세로위치와 가로위치/ L은 탈출 후 소요시간

    # 터널구조
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    # 방문 체크
    visited = [[0] * M for _ in range(N)]
    # 탈주범이 위치할 수 있는 위치의 개수
    ans = 0

    bfs(R, C)

    print('#{} {}'.format(tc, ans))
