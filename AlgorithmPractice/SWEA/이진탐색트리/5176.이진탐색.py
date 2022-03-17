import sys
sys.stdin = open('sample_input.txt', 'r')

def binary_tree(num):
    global number

    if num <= N:
        # 왼쪽 노드는 현재 인덱스 값의 2배
        binary_tree(num*2)
        # 더이상 가지 못하면 값을 넣는다.
        tree[num] = number
        # 값을 넣었으면 숫자를 1 증가시킨다.
        number += 1
        # 우측 노드는 현재 인덱스 값의 2배 +1
        binary_tree(num*2 + 1)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree = [0 for _ in range(N+1)] # 0번 노드는 사용하지 않음

    number = 1 # 숫자를 하나씩 채워 넣어야 하기 때문

    binary_tree(number) # 1부터 시작이기 때문

    # tree의 인덱스는 노드 번호이다.
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))
