import sys
sys.stdin = open('sample_input.txt', 'r')

def dfs(cnt, curr, total):
    global ans
    # 종료 조건(N회차에 사무실로 돌아오기)
    if cnt == N:
        total += arr[curr][0]
        # 최소값 구하기
        if total < ans:
            ans = total
            return

    # 가지치기
    if total > ans:
        return

    # 다음 구역 방문
    for next in range(1, N):
        # n,n 은 값이 0이니 넘어가고 방문을 안 했을 때
        if arr[curr][next] != 0 and visited[next] == 0:
            # 방문 처리
            visited[next] = 1
            # 다음 구역 이동
            dfs(cnt+1, next, total + arr[curr][next])
            # 다 이동 하면 초기화
            visited[next] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 987654321

    # 1회차부터 방문 시작
    dfs(1, 0, 0)

    print('#{} {}'.format(tc, ans))