import sys
sys.stdin = open('sample_input.txt', 'r')

# 고지식한 방법의 패턴매칭
def Bruteforce(str1, str2): # str1이 찾을 문자 str2가 전체 텍스트
    N = len(str1)
    M = len(str2)

    i = 0 # str1의 인덱스
    j = 0 # str2의 인덱스

    while i < N and j < M:
        if str2[j] != str1[i]:
            j = j - i
            i = -1
        j = j + 1
        i = i + 1
    if i == N:
        return True

T = int(input())

for tc in range(1, T+1):
    A,B = map(str, input().split()) # A는 전체 문자, B는 찾는 문자

    # 찾을 문자를 발견한 횟수
    cnt = 0

    while True:
        if Bruteforce(B, A):
            # 전체문자에서 찾는 문자를 찾을 때마다 하나씩 빼기
            A = A.replace(B, '', 1)
            cnt += 1
        else:
            break

    # 남은 문자의 개수 + 찾는 문자를 발견한 횟수
    ans = len(A) + cnt

    print('#{} {}'.format(tc, ans))




