import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    max_value = 0
    min_value = 987654321

    # 구간의 시작 위치
    for i in range(N-M+1): #3개의 인덱스씩 확인하기
        temp = 0
        for j in range(M):
            temp += nums[i+j]

        if max_value < temp:
            max_value = temp
        if min_value > temp:
            min_value = temp

    print('#{} {}'.format(tc, max_value - min_value))


