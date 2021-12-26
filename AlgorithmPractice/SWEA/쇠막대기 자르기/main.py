import sys
sys.stdin = open('sample_input (1).txt', 'r')

T = int(input())

for tc in range(1, T+1):
    blank = str(input())

    stack = []
    cnt = 0

    for i in range(len(blank)):
        # 열린 괄호면 스택
        if blank[i] == '(':
            stack.append('(')
        else:
        # 스택에서 빼기
            stack.pop()
            if blank[i-1] == '(': # 얘는 레이저
                cnt += len(stack)
            else:
                cnt += 1

    print('#{} {}'.format(tc, cnt))

