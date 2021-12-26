import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split()) # N은 노드개수, M은 리프노드 개수, L은 출력할 노드 번호

    tree = [0 for _ in range(N+1)]

    for i in range(M):
        node_num, num = map(int, input().split())
        tree[node_num] = num

    for i in range(N, 0, -1): # 리프노드부터 더하기 때문에 거꾸로 간다.
        if i // 2 > 0: # 노드의 높이가 0이 아닐때까지
            tree[i//2] += tree[i] # 부모 노드는 자식 노드의 합

    print('#{} {}'.format(tc, tree[L]))

# 다른 풀이




