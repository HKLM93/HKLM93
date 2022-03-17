import sys
input = sys.stdin.readline

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


N, M = map(int, input().split()) # N: 세로크기, M: 가로크기
r, c, d = map(int, input().split()) # 로봇청소기의 좌표 r, c / 로봇청소기의 방향 d(0은 북쪽, 1은 동쪽, 2는 남쪽, 3은 서쪽)
field = [list(map(int, input().split())) for _ in range(N)]

field[r][c] = 2 # 처음 청소
ans = 1

while True:
    flag = False  # 방문 체크

    for _ in range(4):
        nd = (d + 3) % 4
        nr = r + dr[nd]
        nc = c + dc[nd]
        d = nd
        # 범위 안에서 움직일 때
        if 0 <= nr < N and 0 <= nc < M:
            if field[nr][nc] == 0:  # 청소를 안 했으면
                ans += 1  # 청소한 칸 추가
                field[nr][nc] = 2  # 청소 처리
                r, c = nr, nc
                flag = True  # 방문처리
                break
    # 4방향을 확인했음에도 청소할 공간이 없는 경우 후진
    if not flag:
        nr = r - dr[d]
        nc = c - dc[d]

        if 0 <= nr < N and 0 <= nc < M:
            if field[nr][nc] == 2:
                r, c = nr, nc
            elif field[nr][nc] == 1:
                print(ans)
                break
