T = int(input())

for tc in range(1, T+1):
    N = int(input())
    Num_list = list(map(int, input().split()))


    for i in range(0, len(Num_list)-1):
        min_idx = i
        for j in range(i+1, len(Num_list)):
            if Num_list[min_idx] > Num_list[j]:
                min_idx = j
        Num_list[i], Num_list[min_idx] = Num_list[min_idx], Num_list[i]

    ans = ' '.join(map(str, Num_list))

    print('#{} {}'.format(tc, Num_list))
