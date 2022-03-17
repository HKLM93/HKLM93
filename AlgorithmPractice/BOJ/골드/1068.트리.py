import sys
input = sys.stdin.readline

def dfs(delete, tree):
    tree[delete] = -2 # 지워야 할 노드를 -2로 표현
    for i in range(len(tree)):
        if delete == tree[i]:
            dfs(i, tree)

N = int(input())
tree = list(map(int, input().split()))
delete = int(input())

# 지워야할 노드 찾기
dfs(delete, tree)

cnt = 0
# 지워야할 노드가 아니고 다른 노드의 부모노드가 아닐 때 카운트
for i in range(len(tree)):
    if tree[i] != -2 and i not in tree:
        cnt += 1

print(cnt)