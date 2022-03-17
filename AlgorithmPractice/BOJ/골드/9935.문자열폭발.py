import sys
input = sys.stdin.readline

text = input().strip()
target_text = input().strip()

# 전체 문자열의 뒤에서부터 접근하여 해당 문자 삭제
# text = list(input().rstrip())
# target_text = list(input().rstrip())
# for i in range(len(target_text)):
#     for j in range(len(text)-1, -1, -1):
#         if target_text[i] == text[j]:
#             text.remove(target_text[i])
# if text:
#     ans = ''.join(text)
#     print(ans)
# else:
#     print('FRULA')
#  -> 시간 초과 ㅠㅠ

# 모범 답안(스택 활용)
stack = []
n = len(text)
m = len(target_text)
for char in text:
    stack.append(char)
    if char == target_text[-1] and ''.join(stack[-m:]) == target_text:
        del stack[-m:]

if len(stack) == 0:
        print("FRULA")
else:
    print("".join(stack))


