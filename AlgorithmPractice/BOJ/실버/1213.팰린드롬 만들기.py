import sys
input = sys.stdin.readline

name = input()
# name = 'ACDEGHRITBFYATEMBPRHFCDGIMP'

alpha_count = [0] * 26 # 26개의 알파벳들 중 무엇을 몇개 사용했는지 알기 위해서

# 포인트는 input문자에서 중복 되는 문자가 홀수개를 가지느냐 짝수개를 가지느냐를 찾는 것
for char in name:
    alpha_count[ord(char) - 65] += 1 # 알파벳을 아스키코드표로 숫자로 변환시켜 인덱스를 표시(A = 65)

odd_cnt = 0 # 홀수개를 가지는 중복 문자가 2개 이상이면 회문을 만들 수 없어서 이를 확인해야 한다
odd_str = '' # 홀수개인 문자를 출력하기 위함
ans = '' # 짝수개인 문자를 출력하기 위함

for i in range(26):
    if alpha_count[i] % 2 == 1: # 홀수인 값을 찾기
        odd_cnt += 1
        odd_str += chr(i+65) # 홀수개인 문자
    ans += chr(i+65) * (alpha_count[i]//2) # 짝수개인 문자의 절반

reversed_ans = ans+odd_str+ans[::-1] # 짝수개 문자 + 홀수개 문자 + 짝수개 문자를 뒤집은 문자

if odd_cnt > 1: # 홀수개를 가지는 중복문자가 2개 이상이면 회문 불가
    print('I\'m Sorry Hansoo')
else:
    print(reversed_ans)


