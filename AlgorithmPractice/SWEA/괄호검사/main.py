import sys
sys.stdin = open('sample_input.txt','r')

# 스택 함수
def check_bracket(text):
    text_stack =[]
    for w in text:
        # 주어진 문자를 순회
        if w == '(' or w =='{': # 여는 괄호가 있으면 스택에 넣음
            text_stack.append(w)
        elif w == ')' or w =='}':
            # 처음부터 닫는 괄호가 나오는 경우
            if len(text_stack) == 0:
                text_stack.append(w)
                break
            # stack에 저장된 괄호와 일치하지 않는 경우
            elif w == ')' and text_stack[-1] != '(' or w =='}' and text_stack[-1] != '{':
                text_stack.append(w)
                break
            # stack에 저장된 괄호와 일치하는 경우
            else:
                text_stack.pop(-1)
    # 스택에 값이 존재할 때
    if text_stack:
        return 0
    # 스택에 값이 없을 때
    else:
        return 1

T = int(input())

for tc in range(1, T+1):
    test_case = str(input())

    print('#{} {}'.format(tc,check_bracket(test_case)))