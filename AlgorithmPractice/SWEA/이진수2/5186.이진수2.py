import sys
sys.stdin = open('sample_input.txt', 'r')

# 소수점의 2진수 표현은 10진수 소수 * 2 값이 1보다 크면 1, 작으면 0이다.
def make_binary(num):
    global result
    # 자리수를 세기 위함(while문을 1번 돌면 자리수가 1개 추가됨)
    cnt = 0
    while num:
        next_num = num * 2
        result += str(int(next_num))
        num = next_num - int(next_num)
        cnt += 1

        if cnt > 13:
            return 'overflow'
    return result

T = int(input())
for tc in range(1, 1+T):
    N = float(input())
    result = ''

    print('#{} {}'.format(tc, make_binary(N)))


