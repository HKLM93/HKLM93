import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 행 순회로 1이 K번 연속되는 횟수를 구함
    ans = 0 # 단어를 찾는 경우 초기화
    for i in range(len(arr)):
        cnt = 0 # 1이 있을 때 개수를 세기 위함
        for j in range(len(arr[i])-1, -1, -1):
            if arr[i][j] == 1:
                cnt += 1 # 1의 개수를 누적
            if arr[i][j] == 0 or j == 0: # 0을 만나거나 가장 끝에 갔을 때
                if cnt == K:
                    ans += 1
                cnt = 0 # 카운트를 초기화

    # 열 순회로 1이 K번 연속되는 횟수를 구함
    for j in range(len(arr[0])):
        cnt = 0
        for i in range(len(arr) - 1, -1, -1):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 0 or i == 0:
                if cnt == K:
                    ans += 1
                cnt = 0

    print('#{} {}'.format(tc, ans))


