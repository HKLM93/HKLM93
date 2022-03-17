import sys
sys.stdin = open('sample_input.txt', 'r')

# 전위순회
def preorder(node):
    global cnt

    if node:
        cnt += 1
        preorder(left[node])
        preorder(right[node])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split()) # E는 간선의 개수, N은 서브트리의 루트노드의 번호
    tree = list(map(int, input().split()))

    left = [0] * (E+2) # 0번은 사용하지 않음
    right = [0] * (E+2) # 0번은 사용하지 않음

    for i in range(0, len(tree), 2):
        parent, child = tree[i], tree[i+1] # 부모노드, 자식노드 나누기
        # 왼쪽 자식에 값이 있으면 오른쪽 자식에 넣는다.
        # 결과는 해당하는 인덱스의 자식의 값(문제에 나온 표의 모습)
        if left[parent] != 0:
            right[parent] = child
        else:
            left[parent] = child

    cnt = 0 # subtree에 있는 노드를 세기 위함
    preorder(N)

    print('#{} {}'.format(tc, cnt))




