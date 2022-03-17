import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    formula = input().split()

    result = ''  # 연산결과를 담을 빈 문자
    stack = []  # 피연산자를 담을 스택
    
    try:
        for i in range(len(formula)):
            if formula[i] == '+':
                A = stack.pop()
                B = stack.pop()
                stack.append(B+A) # 먼저 pop한 값이 뒤로 가야한다.
            elif formula[i] == '*':
                A = stack.pop()
                B = stack.pop()
                stack.append(B*A)
            elif formula[i] == '-':
                A = stack.pop()
                B = stack.pop()
                stack.append(B-A)
            elif formula[i] == '/':
                A = stack.pop()
                B = stack.pop()
                stack.append(B//A)
            elif formula[i] == '.':
                result = stack.pop()
                if len(stack) != 0: # 스택에 값이 남아 있을 경우
                    print('#{} {}'.format(tc, 'error')) 
                    break
                else:
                    print('#{} {}'.format(tc, result))
            else:
                numbers = int(formula[i])
                stack.append(numbers) # 피연산자를 스택에 넣는다.
    except: # 오류는 전부 error가 출력 되게 설정
        print('#{} {}'.format(tc, 'error'))



