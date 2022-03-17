import sys
sys.stdin = open('sample_input.txt', 'r')


# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# dfs 활용
def make_road(r, c, h, road, skill):
    global max_length
    # 산책로의 최대값
    if road > max_length:
        max_length = road

    visited[r][c] = 1 # 시작점 방문표시

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        # 범위를 넘어가거나 방문했으면 통과
        if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc] == 1:
            continue

        # 다음위치가 높이보다 작으면 방문, 산책로 +1
        if h > field[nr][nc]:
            # visited[nr][nc] = 1
            make_road(nr, nc, field[nr][nc], road+1, skill)

        # 갈 수 없으면 공사를 함(1~K까지) 그리고 dfs
        elif skill and h > field[nr][nc] - K:
            make_road(nr, nc, field[r][c]-1, road+1, 0)

    visited[r][c] = 0 # 방문 초기화


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) # N은 변의 길이, K는 최대 공사 가능 깊이
    field = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    max_height = 0 # 최소 높이가 1이기 때문에 더 작은 0을 초기값으로 설정
    for i in range(N):
        for j in range(N):
            if field[i][j] > max_height:
                max_height = field[i][j]

    max_length = 0 # 산책로 최대값을 구하기 위한 초기값

    for i in range(N):
        for j in range(N):
            if field[i][j] == max_height:
                make_road(i, j, max_height, 1, 1) # 좌표의 행, 좌표의 열, 최대높이, 등산로 거리, 스킬(공사여부)
    print('#{} {}'.format(tc, max_length))



