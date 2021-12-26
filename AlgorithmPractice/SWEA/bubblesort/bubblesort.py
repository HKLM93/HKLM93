# Bubble-sort 오름차순 정렬
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):  # Test_case T번 만큼 반복
    N = int(input())  # 숫자열의 길이
    list_num = list(map(int, input().split()))  # 숫자열 리스트

    for i in range(len(list_num) - 1, 0, -1):  # list_num을 뒤에서부터 순회하기, j+1이 있어서 인덱스 오류를 막기 위해 -1을 빼줌
        for j in range(0, i):
            if list_num[j] > list_num[j + 1]:  # 앞에서부터 두개씩 비교하기 위함
                list_num[j], list_num[j + 1] = list_num[j + 1], list_num[j]  # 크기 비교 후 큰 값이 오름차순으로 정렬될 수 있도록 값을 서로 바꿈

    ans = ' '.join(map(str, list_num))

    print('#{} {}'.format(tc, ans))



