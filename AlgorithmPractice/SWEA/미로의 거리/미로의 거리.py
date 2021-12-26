import sys
sys.stdin = open('sample_input.txt', 'r')

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def BFS(r, c):
    global path

    visited[r][c] = path
    queue = [(r, c)]
    distance = [[0] * N for _ in range(N)] # 거리를 계산할 2차원 리스트

    while queue:
        start_r, start_c = queue.pop(0)

        for i in range(4):
            nr = start_r + dr[i]
            nc = start_c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N: # 범위를 벗어나지 않도록
                continue

            if maze[nr][nc] == 0 and visited[nr][nc] == 0:
                queue.append((nr, nc))
                visited[nr][nc] = path
                distance[nr][nc] = distance[start_r][start_c] + 1 # 갈 수 있으면 거리에 1 더하기
            if maze[nr][nc] == 3: # 도착하면 거리 값을 출력
                return distance[start_r][start_c]

    return 0 # 3에 도착하지 못했을 때

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    path = 1 # 벽이거나 갔던 길이라 가지 못하는 길

    # 시작점의 행렬 인덱스와 도착점의 행렬 인덱스를 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 1: # 미로에 있는 벽을 visted에도 세우기
                visited[i][j] = 1
            if maze[i][j] == 2 and visited[i][j] == 0:
                ans = BFS(i, j)


    print('#{} {}'.format(tc, ans))

