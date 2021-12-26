import sys
sys.stdin = open('sample_input.txt', 'r')

def is_safe(r, c):
    return 0<= r <N and 0<= c <N and (maze[r][c] == 0 or maze[r][c] == 3) # 이동할 수 있는 곳을 제한

def DFS(r, c):
    global ans

    if maze[r][c] == 3: # 3에 도착하면 결과 출력
        ans = 1
        return

    visited.append((r, c)) # 현재위치
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if is_safe(nr, nc) and (nr, nc) not in visited: # 벽을 넘어가지 않게 범위 설정, 갔던 곳을 다시 돌아가지 않게 설정
            DFS(nr, nc)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 시작점의 행렬 인덱스와 도착점의 행렬 인덱스를 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_r, start_c = i, j

    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited = []
    ans = 0

    DFS(start_r, start_c)
    print('#{} {}'.format(tc, ans))




