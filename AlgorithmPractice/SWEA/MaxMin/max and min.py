
T = int(input())


for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))


    max_value = num_list[0]
    min_value = num_list[0]

    for i in range(1, len(num_list)):
        # 최대값 구하기
        if max_value < num_list[i]:
            max_value = num_list[i]

        # 최소값 구하기
        if min_value > num_list[i]:
            min_value = num_list[i]

    ans = max_value - min_value

    print('#{} {}'.format(tc, ans))

