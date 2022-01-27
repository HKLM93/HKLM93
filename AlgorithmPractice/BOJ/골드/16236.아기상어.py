import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):

    visited = [[0]*N for _ in range(N)]
    visited[r][c] = 1
    queue = deque()
    queue.append([r, c, 0]) # 상어의 위치와 거리를 저장
    distance = []
    min_dist = 987654321

    while queue:
        r, c, dist = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위를 벗어나지 않고 방문 안 했을 때
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc]== 0:
                # 물고기가 있거나 빈 장소라면
                if area[nr][nc] <= size:
                    visited[nr][nc] = 1
                    # 상어의 크기보다 물고기가 작거나 같다면
                    if 0 < area[nr][nc] < size:
                        # 최소거리 갱신
                        min_dist = dist
                        # 거리, 물고기 위치를 저장
                        distance.append([dist+1, nr, nc])
                    # 갈 수 있으면
                    if dist + 1 <= min_dist:
                        # 다음 위치 저장
                        queue.append([nr, nc, dist+1])
    if distance:
        # 먹을 수 있는 물고기들을 왼쪽부터 먹도록 정렬
        distance.sort()
        return distance[0]
    # 먹을 수 있는 물고기가 없다면
    else:
        return False


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

size = 2
ans = 0 # 움직인 거리
fish_cnt = 0 # 물고기의 개수
fish_pos = [] # 물고기의 위치
eat = 0 # 먹은 물고기의 개수

for i in range(N):
    for j in range(N):
        if 0 < area[i][j] <= 6:
            fish_cnt += 1
            fish_pos.append([i, j])
        elif area[i][j] == 9:
            shark_r, shark_c, = i, j # 상어의 위치 저장
area[shark_r][shark_c] = 0 # 상어가 움직이면 그 공간은 비게 됨

while fish_cnt:
    result = bfs(shark_r, shark_c)

    # 물고기를 못 먹었을 때
    if not result:
        break
    # 물고기를 먹었으면 상어 위치 갱신
    shark_r, shark_c = result[1], result[2]
    # 최소거리 더해줌
    ans += result[0]
    eat += 1
    fish_cnt -= 1
    # 상어의 크기만큼 먹었으면
    if size == eat:
        # 사이즈가 커짐
        size += 1
        # 먹은 거 초기화
        eat = 0
    # 상어위치는 다시 방문하지 않을 것으로 처리
    area[shark_r][shark_c] = 0

print(ans)
