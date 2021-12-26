# 스택 함수 만들기
stack_list = []

# push
stack_list.append(1)

# peek(공백 검사를 진행한 후 봐야 함)
if len(stack_list) > 0:  # 스택이 빈리스트가 아닐 때
    stack_list[-1]
    stack_list[len(stack_list)-1]

# pop(공백 검사 후 꺼내야 한다)
if len(stack_list) > 0:
    stack_list.pop()
    stack_list.pop(-1)
    stack_list.pop(len(stack_list)-1)

######################################################


# 일반적인 언어에서 배열을 이용하여 사용한 경우는
stack_arr = [0] * 1000000
top = -1 # 마지막 원소를 가리킨다

# push(가득 차 있는지 검사를 한 다음 넣어야 한다)
if len(stack_arr) -1 > top:
    top += 1
    stack_arr[top] = 1

# peek 공백 검사 후 확인
if top > -1:
    stack_arr[top]

# pop 공백 검사 후 확인
if top >= 0:
    N = stack_arr[top]
    top -= 1