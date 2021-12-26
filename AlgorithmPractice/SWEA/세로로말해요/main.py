import sys
sys.stdin = open('sample_input.txt', 'r')


T = int(input())

for tc in range(1, T+1):
    word = [0] * 5
    max_len = 0

    for i in range(5):
        word[i] = list(input())
        if len(word[i]) > max_len:
            max_len = len(word[i])

    print('#{}'.format(tc), end=' ')

    for i in range(max_len):
        for j in range(5):
            # 1. 허락 받고 쓰자
            if len(word[j]) > i:
                print(word[j][i], end='')
    print()
            # 2. 용서를 구하자
            # try:
            #   print(word[j][i], end='')
            # except:
            #   pass







# 내 방법(런타인 오류 나옴)
# T = int(input())
# for tc in range(1, T + 1):
#     arr = [input() for _ in range(5)]
#
#     # 문자열 중 가장 긴 문자열의 길이를 찾기
#     max_len = len(arr[0])
#     for idx in range(1, len(arr)):
#         if len(arr[0]) < len(arr[idx]):
#             max_len = len(arr[idx])
#
#     # 가장 긴 문자열을 크기로 가지는 ㄱ 리스크 생성 - 문제에서 사용하는 문자들이 영어와 숫자라서 나중에 지울 때 겹치지 않기 위해
#     new_list = [['ㄱ'] * max_len for _ in range(5)]
#     # test case 리스트를 ㄱ 리스트에 집어 넣기
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             new_list[i][j] = arr[i][j]
#
#     # 열 순회
#     result = ''
#     for j in range(len(new_list[0])):
#         for i in range(len(new_list)):
#             result += new_list[i][j]
#
#     # ㄱ은 input리스트에서 빈자리를 의미 하기 때문에 지워줌
#     ans = result.replace('ㄱ','')
#
#     print('#{} {}'.format(tc, ans))
