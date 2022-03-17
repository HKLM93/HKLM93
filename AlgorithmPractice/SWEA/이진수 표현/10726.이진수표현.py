import sys
sys.stdin = open('input.txt', 'r')

# 2진수를 만드는 함수
def make_binary(num):
    global N
    # 뒤에서 N개의 비트가 1인지만 확인하면 됨
    for i in range(N):
        # 0이 있으면 OFF출력
        if num % 2 == 0:
            return 'OFF'
        # 2로 나눔
        num //= 2
    # N번 나누어서 0이 없으면 전부 1이니 ON출력
    else:
        return 'ON'

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())

    print('#{} {}'.format(tc, make_binary(M)))

