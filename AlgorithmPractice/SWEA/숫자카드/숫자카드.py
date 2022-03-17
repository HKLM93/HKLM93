import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input()))
    cnt_list = [0] * 10
    cnt = 0 #카드 번호
    max_value = 0 #카드 개수

    #카운팅 하기
    for i in num_list:
        cnt_list[i] += 1

    # 카운팅 개수 리스트에서 max값 찾기
    for j in range(len(cnt_list)-1, -1, -1):
        if cnt_list[j] > max_value: #앞에서부터 접근하면 >=로 해야한다.
            max_value = cnt_list[j]
            cnt = j

    print('#{} {} {}'.format(tc, cnt, max_value))



