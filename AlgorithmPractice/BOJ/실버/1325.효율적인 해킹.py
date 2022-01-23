import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    cnt = 1
    visited = [0] * (N+1)
    visited[start] = 1

    queue = deque()
    queue.append(start)

    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if not visited[next]:
                queue.append(next)
                visited[next] = 1
                cnt += 1
    return cnt

N, M = map(int, input().split()) # N:회사의 컴퓨터 개수(정점), M: 연결관계의 수

graph = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n2].append(n1) # 방향성 존재

result = []
max_cnt = 0
for i in range(1, N+1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
    result.append([i, cnt])

for j in result:
    if j[1] == max_cnt:
        print(j[0], end=' ')