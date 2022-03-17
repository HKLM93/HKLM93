import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int,input().split())

    # A 리스트는 1~12를 가지고 있는 집합
    A = list(range(1,13))
    # 합이 K일 경우 cnt를 세기 위함
    cnt = 0
    # 부분집합들의 리스트
    _list=[]
    # 부분집합 만들기
    for i in range(1 << len(A)):
        sub_list = []
        # i는 부분집합의 경우의 수 이진수로 생각
        for j in range(len(A)):
            if i & (1 << j):
                sub_list.append(A[j])
        _list.append(sub_list)

    # 부분집합들의 합 구하기
    for k in _list:
        _list_sum = 0
        for l in k:
            _list_sum += l
        # 부분집합의 길이가 N이고 부분집합의 합이 K일 때 카운트
        if len(k) == N and _list_sum == K:
            cnt += 1

    print('#{} {}'.format(tc, cnt))







