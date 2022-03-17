import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    # str2에 있는 문자가 str1가 있다면 포함하는 횟수를 담을 빈 리스트
    cnt_list = []

    # str1과 str2를 순회하면서 확인
    for i in range(len(str1)):
        cnt = 0 # str1이 str2에 있는 횟수 초기화
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt += 1
        cnt_list.append(cnt)

    # 횟수들 중 최대값 구하기
    max_value = cnt_list[0]

    for i in range(1, len(cnt_list)):
        if cnt_list[i] > max_value:
            max_value = cnt_list[i]

    print('#{} {}'.format(tc,max_value))










