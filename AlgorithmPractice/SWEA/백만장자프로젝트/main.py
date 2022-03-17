import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    days = list(map(int, input().split()))

    # 시세 리스트를 뒤에서부터 접근하도록 함
    sum_buy = 0
    reversed_days = days[::-1]
    now_max = reversed_days[0]
    # 뒤에서부터 읽으면서 최댓값을 구하고 (최대값-매매값)을 누적함
    for j in range(1, len(reversed_days)):
        if now_max > reversed_days[j]:
            sum_buy += now_max - reversed_days[j]
        # 새로운 최대값이 나오면 최대값을 갱신
        else:
            now_max = reversed_days[j]

    print('#{} {}'.format(tc, sum_buy))




