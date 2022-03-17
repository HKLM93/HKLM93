import sys
sys.stdin = open('sample_input.txt', 'r')


def DFS(idx):
    global sum, min
    # 최소값 구하기
    if idx == N:
        if sum < min:
            min = sum
        return
    # 가지치기
    if sum > min:
        return

    for j in range(0, N):
        if visited[j] == 0: # 접근한 적이 없다면
            sum += arr[idx][j]

            visited[j] = 1 # 접근한 것으로 바꾸기

            DFS(idx+1)

            visited[j] = 0 # 초기화
            sum -= arr[idx][j] # 최소값이 아닐 경우 더했던 값을 빼면서 합 초기화


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    visited = [0] * N # 행의 중복을 막기 위함

    sum = 0
    min = 999999 # 최소값을 큰 값으로 설정해 비교

    DFS(0)

    print('#{} {}'.format(tc, min))



