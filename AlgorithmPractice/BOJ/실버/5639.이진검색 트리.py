import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

def postorder(start, end):
    # 왼쪽이 오른쪽 보다 작아서
    if start > end:
        return
    else:
        # 루트 노드
        root = preorder[start]
        # 루트 노드는 인덱스 0번이라 0번과 1번 비교를 위해
        div = end + 1
        #
        for i in range(start+1, end+1):
            if preorder[i] > root:
                div = i
                break

        postorder(start+1, div-1)
        postorder(div, end)
        print(root)

preorder = []

while True:
    try:
        preorder.append(int(input()))
    except:
        break

postorder(0, len(preorder)-1)


