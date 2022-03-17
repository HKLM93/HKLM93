import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Nums = list(map(int,input().split()))

    for i in range(M): # M번을 회전
        Nums.append(Nums.pop(0)) # 가장 앞의 인덱스 값을 빼서 뒤로 넣는다.

    print('#{} {}'.format(tc, Nums[0]))

