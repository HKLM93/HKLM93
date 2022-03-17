import sys
sys.stdin = open('sample_input.txt', 'r')

# 하, 우 이동
dr = [1, 0]
dc = [0, 1]

def find_min(r, c, result):
    global min_sum
    # 도착했을 때
    if r == N-1 and c == N-1:
        # 마지막 값을 더해준다
        result += arr[r][c]
        # 합의 최소값 갱신
        if result < min_sum:
            min_sum = result
            return

    # 가지치기(지금 계산하는 경로가 최소값보다 작으면 계산할 필요가 없다)
    if result > min_sum:
        return

    # 방문 표시
    visited[r][c] = 1

    # 오른쪽과 아래로만 갈 수 있다
    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]

        # 범위를 벗어나면
        if nr >= N or nc >= N or visited[nr][nc] == 1:
            continue

        # 방문한 적이 없으면
        if visited[nr][nc] == 0:
            # 방문 표시
            visited[nr][nc] = 1
            # 다음 좌표 계산과 현재 값을 더해준다
            find_min(nr, nc, result + arr[r][c])
            # 돌아왔으면 방문 초기화
            visited[nr][nc] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    # 최소값을 구하기 위해 충분히 큰 값으로 초기값을 설정
    min_sum = 987654321
    # 합을 구하기 위한 초기값
    result = 0

    find_min(0, 0, result)

    print('#{} {}'.format(tc, min_sum))
