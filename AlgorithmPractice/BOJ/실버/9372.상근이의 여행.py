import sys
from collections import deque

def bfs(S):
    queue = deque()
    queue.append(S)
    visited[S] = 1
    cnt = 0

    while queue:
        t = queue.popleft()

        for i in tree[t]:
            if visited[i] == 0:
                visited[i] = 1
                cnt += 1
                queue.append(i)
    return cnt


T = int(sys.stdin.readline())

for tc in range(T):
    N, M = map(int, sys.stdin.readline().split()) # N은 국가의 수(노드의 수), M은 비행기의 종류(간선의 수)

    tree = [[] for _ in range(N+1)]
    visited = [0] * (N + 1)

    for i in range(M):
        a, b = map(int, sys.stdin.readline().split()) # a,b는 연결된 노드
        tree[a].append(b)
        tree[b].append(a)

    ans = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            ans += bfs(i)
    print(ans)

    # 모든 그래프가 연결되어 있어서 굳이 한 번더 포문을 안 돌리고
    # print(bfs(1))을 해도 될 거 같다

