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
        return list(str1)

T = int(input())

for tc in range(1, T+1):
    A, B = map(str, input().split()) # A가 전체 텍스트, B가 찾을 문자

    str_A = list(A)
    str_B = list(B)

    if Bruteforce(str_B, str_A) in str_A:






