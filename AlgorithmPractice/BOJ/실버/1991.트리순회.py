import sys

def preorder(root): # 전위순회
    if root != '.':
        print(root, end='') # root 순회
        preorder(tree[root][0]) # left 순회
        preorder(tree[root][1]) # right 순회

def inorder(root): # 중위순회
    if root != '.':
        inorder(tree[root][0]) # left 순회
        print(root, end='') # root 순회
        inorder(tree[root][1]) # right 순회

def postorder(root): # 후위순회
    if root != '.':
        postorder(tree[root][0]) # left 순회
        postorder(tree[root][1]) # right 순회
        print(root, end='')  # root 순회

N = int(sys.stdin.readline())
tree = {}

for i in range(N):
    root, left, right = map(str, sys.stdin.readline().split())
    tree[root] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')
