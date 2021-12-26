import sys
sys.stdin = open('sample_input.txt', 'r')

def min_heap(node):
    tree.append(node)
    idx = len(tree) -1 # 0을 안 쓰기 때문에 -1을 해준다.
    while idx > 1 and tree[idx] < tree[idx//2]: # 루트까지 올라가고 최소 힙의 조건을 만족할 때까지 반복
        tree[idx], tree[idx//2] = tree[idx//2], tree[idx] # 부모노드와 자식노드를 비교해서 부모노드가 크면 자식노드와 바꾼다
        idx //= 2 # 가장 아래에서 시작했기 때문에 다음을 비교하기 위해 높이를 -1하도록 만든다.

def node_sum():
    total = 0
    idx = N // 2 # 트리의 높이(마지막 노드의 조상 노드들의 합이기 때문에 이렇게만 구해도 된다)
    while idx:
        total += tree[idx] # 해당하는 값을 더함
        idx //= 2
    return total

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 노드의 개수
    input_list = list(map(int, input().split()))
    tree = [0] # 0번 인덱스는 사용하지 않음

    ans = 0 # 답을 구하기 위한 합의 초기값
    for i in input_list:
        min_heap(i)
    ans = node_sum()

    print('#{} {}'.format(tc, ans))









