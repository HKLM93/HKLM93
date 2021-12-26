import sys
sys.stdin = open('sample_input.txt', 'r')

def up_bubble_sort(Nums):
    for i in range(len(Nums)-1, 0, -1):
        for j in range(0, i):
            if Nums[j] > Nums[j+1]:
                Nums[j], Nums[j+1] = Nums[j+1], Nums[j]
    return Nums

def down_bubble_sort(Nums):
    for i in range(len(Nums)-1, 0, -1):
        for j in range(0, i):
            if Nums[j] < Nums[j+1]:
                Nums[j], Nums[j+1] = Nums[j+1], Nums[j]
    return Nums


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    Num_list = list(map(int, input().split()))

    ans_list = [0] * N

    even_idx =
    odd_idx = -1

    # 홀수 인덱스는 오름차순, 짝수 인덱스는 내림차순





    print(ans_list)


