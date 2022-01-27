from collections import deque
import sys

def bfs(S):
    global visited
    queue = deque([S])
    visited[S] = 1

    while queue:
        t = queue.popleft()

        for i in range(1, N+1):
            if adj_arr[t][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1

N, M = map(int, sys.stdin.readline().split()) # N은 노드의 개수, M은 간선의 개수
adj_arr = [[0]*(N+1) for _ in range(N+1)] # 0번 노드는 사용하지 않음
visited = [0] * (N + 1)

for i in range(M):
    u, v = map(int, sys.stdin.readline().split()) # 간선의 양 끝점
    adj_arr[u][v] = 1
    adj_arr[v][u] = 1 # 방향이 없는 그래프

cnt = 0 # 연결된 노드들의 그룹의 개수를 세기 위함

for i in range(1, N+1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)

