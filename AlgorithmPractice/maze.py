# 미로 찾기 1. 모든 칸을 방문
from typing import MappingView


def f1(i, j, N): # 모든 칸을 방문하는 탐색
    maze[i][j] = 2 # 디버거로 볼 때는 2로하면 편함 # i, j 방문표시.(진입한 칸을 벽으로 변경)
    # visited[i][j] = 1 (visited를 사용할 경우)
    for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]: # 4방향 탐색
        ni, nj  = i + di, j + dj
        # 탐색방향이 통로이면
        if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] ==0: # and visited[ni][nj] ==0 # ni,nj조건과 인덱스 조건은 위치가 바뀌면 안 된다.
            f1(ni, nj, N)

N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
f1(0, 0, N) # 탐색 시작 (0,0), 미로의 크기 N
# visited = [[0] * N for _ in range(N)] # visited를 사용할 경우(원본맵을 바꾸는 방법이다)
print(maze[N-1][N-2])

# 미로 찾기 2. 출구를 찾으면 중단
def f2(i, j, N): # 출구를 찾으면 중단
    if i == N-1 and j == N-1: # 출구에 도착한 경우
        return 1
    else:
        maze[i][j] = 2 # i, j 방문표시(진입한 칸을 벽으로 변경)
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]: # 4방향 탐색
            ni, nj  = i + di, j + dj
            # 탐색방향이 통로이면
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] ==0: # and visited[ni][nj] ==0 # ni,nj조건과 인덱스 조건은 위치가 바뀌면 안 된다.
                f2(ni, nj, N)
N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
print(f2(0, 0, N)) 

# 미로 찾기 3. 가능한 경로 찾기
def f3(i, j, N):
    global cnt
    if i == N-1 and j == N-1:
        cnt += 1 # 경로에 도착한 횟수
        return
    else:
        maze[i][j] = 2 # 없으면 무한 루프의 위험
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]: # 4방향 탐색
            ni, nj  = i + di, j + dj
            # 탐색방향이 통로이면
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] ==0:
                f3(ni, nj, N)
        maze[i][j] = 0 # 다른 경로에서의 i, j 진입은 허용 
N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
f3(0, 0, N)
print(cnt)

# 미로 찾기 4. 최단 거리
def f4(i, j, N, c): # c는 지나온 칸의 개수, 최단 거리를 찾기 위해 + 모든 경로 탐색
    global minV
    if i == N-1 and j == N-1:
        if minV > c+1: # 기존경로보다 도착지 포함 경로의 길이가 더 짧으면
            minV = c+1 # c+1 출발, 도착을 포함한 경로의 길이
        return
    else:
        maze[i][j] = 2 # 없으면 무한 루프의 위험
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]: # 4방향 탐색
            ni, nj  = i + di, j + dj
            # 탐색방향이 통로이면
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] ==0:
                f4(ni, nj, N)
        maze[i][j] = 0 # 다른 경로에서의 i, j 진입은 허용 
N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
minV = 0
c = 0
f4(0, 0, N, c)
print(minV)
# 맞는지는 교수님 코드 확인하기




