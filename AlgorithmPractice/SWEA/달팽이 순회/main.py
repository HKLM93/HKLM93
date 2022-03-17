import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 0으로 된 2차원 리스트 먼저 만듦
    arr = [[0] * N for _ in range(N)]

    # 우, 하, 좌, 상 이동
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    #시작 위치, 입력할 숫자, 방향 시작값
    r = 0 # 행좌표
    c = 0 # 열좌표
    num = 1 # 내가 찍을 숫자
    d = 0 # 방향

    # 2차원 리스트 순회
    while num <= N*N:
        arr[r][c] = num
        num += 1

        # 다음 칸 결정
        nr = r + dr[d]
        nc = c + dc[d]

        # 유효한 좌표인지 검사
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            # 무조건 간다
            r, c = nr, nc
        else:
            d = (d+1) % 4
            r += dr[d]
            c += dc[d]
    print('#{}'.format(tc))

    for i in range(N):
        for j in range(N):
            print(arr[i][j], end='')
        print()
