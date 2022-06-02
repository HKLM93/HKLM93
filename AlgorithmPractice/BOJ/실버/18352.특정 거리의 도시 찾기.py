import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    ans = []
    queue = deque([start])
    visited[start] = 1
    distance[start] = 0

    while queue:
        now = queue.popleft()

        for i in graph[now]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == K:
                    ans.append(i)
    # 도시가 없을 때
    if len(ans) == 0:
        print(-1)
    # 도시가 있을 때
    else:
        # 오름차순 출력을 위해
        ans.sort()
        for i in ans:
            print(i, end='\n')


N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [0] * (N+1) # 거리확인
visited = [0] * (N+1) # 방문체크

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2) # 단방향

bfs(X)