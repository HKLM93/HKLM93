import sys
sys.stdin = open('sample_input.txt', 'r')

# 종이 붙이기 점화식
def paper(N):
    if N == 10:
        return 1
    if N ==20:
        return 3
    else:
        return paper(N-10) + (2 * paper(N-20))


T = int(input())

for tc in range(1, T+1):
    n = int(input())

    ans = paper(n)

    print('#{} {}'.format(tc, ans))
