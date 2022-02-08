import sys
from collections import deque
input = sys.stdin.readline

# 우 상 좌 하
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def find_ans(cnt):
    global ans, visited

    # 모든 cctv를 탐색했으면 사각지대 세기
    if cnt == cctv_cnt:
        tmp = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0 and visited[i][j] == 0:
                    tmp += 1
        return tmp

    r, c = cctv[cnt][0], cctv[cnt][1]

    for i in range(4):
        new_dir = []

        # 1번 CCTV
        if arr[r][c] == 1:
            new_dir.append(i)

        # 2번 CCTV
        elif arr[r][c] == 2:
            new_dir.append(i)
            new_dir.append((i+2) % 4)

        # 3번 CCTV
        elif arr[r][c] == 3:
            new_dir.append(i)
            new_dir.append((i-1) % 4)

        # 4번 CCTV
        elif arr[r][c] == 4:
            new_dir.append(i)
            new_dir.append((i-1) % 4)
            new_dir.append((i+2) % 4)

        # 5번 CCTV
        elif arr[r][c] == 5:
            new_dir.append(i)
            new_dir.append((i-1) % 4)
            new_dir.append((i+1) % 4)
            new_dir.append((i+2) % 4)

        queue = deque()

        for d in new_dir:
            nr = r + dr[d]
            nc = c + dc[d]

            # 범위 안에서 방문 하지 않았고 벽이 아니면 갈 수 있다
            while 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == 0 and arr[nr][nc] != 6:
                    visited[nr][nc] = 1
                    queue.append([nr, nc])
                # 벽이면 중단
                elif arr[nr][nc] == 6:
                    break
                nr += dr[d]
                nc += dc[d]

        # 다음 CCTV 호출
        ans = min(ans, find_ans(cnt+1))

        # 방문 했던 곳 되돌리기
        while queue:
            qr, qc = queue.popleft()

            if arr[qr][qc] == 0:
                visited[qr][qc] = 0
        # 5번 CCTV는 회전할 필요가 없다.
        if arr[r][c] == 5:
            break

    return ans

N, M = map(int, input().split()) # N: 세로크기, M: 가로크기
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
cctv = []
cctv_cnt = 0
ans = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] != 6 and arr[i][j] != 0:
            cctv.append([i, j])
            visited[i][j] = 1
            cctv_cnt += 1
        # 최대 사각지대의 개수
        if arr[i][j] == 0:
            ans += 1

find_ans(0)
print(ans)