import sys
sys.setrecursionlimit(10**6)

def dfs(tree, parent, start):
    # 부모노드가 없으면 부모 노드를 설정해주고 dfs
    for i in tree[start]:
        if parent[i] ==0:
            parent[i] = start
            dfs(tree, parent, i)

N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)] # 첫노드는 사용하지 않음
parent = [0 for _ in range(N+1)] # 부모노드 저장

# 트리 구조
for i in range(N-1):
    left, right = map(int, sys.stdin.readline().split())
    tree[left].append(right)
    tree[right].append(left)

dfs(tree, parent, 1)

for i in range(2, N+1):
    print(parent[i])

