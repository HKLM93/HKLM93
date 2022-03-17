nums = [1, 2, 3, 4, 5, 6]

is_ok = False

# 완전탐색 Baby-Gin

for i in range(6):
    for j in range(6):
        if i != j:
            for k in range(6):
                if k != j and k !=i:
                    for l in range(6):
                        if l != k and l != j and l != i:
                            for m in range(6):
                                if m != l and m != k and m !=j and m != i:
                                    for n in range(6):
                                        if n != m and n != l and n != k and n != j and n != i:
                                            print(nums[i], nums[j], nums[k], nums[l], nums[m], nums[n])
                                            left = False
                                            right = False

                                             # 왼쪽을 tri, run 검사를 해보자
                                            if nums[i] == nums[j] and nums[i] == nums[k]:
                                                left = True
                                            elif nums[i] == nums[j]-1 and nums[i] == nums[k]-2:
                                                left = True
                                             # 오른쪽도 tri, run 검사
                                            if left and right:
                                               is_ok = True

# counting 정렬

import sys
sys.stdin=open('sample_input.txt', 'r')

T = int(input())



for tc in range(1, T + 1):

    N = int(input())
    c = [0] * 12

    for i in range(6):
        c[N % 10] += 1
        N //= 10

    i = 0
    tri_num = run_num = 0

    while i < 10:
        if c[i] >= 3:
            c[i] -= 3
            tri_num += 1
            continue
        if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:
            c[i] -= 1
            c[i + 1] -= 1
            c[i + 2] -= 1
            run_num += 1
            continue
        i += 1

    if run_num + tri_num == 2:
        print('#{} {}'.format(tc, '1'))
    else:
        print('#{} {}'.format(tc, '0'))
