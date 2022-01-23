import sys

# DFS
def DFS(S):
    visited[S] = 1
    print(S, end=' ')
    for i in range(1, N+1):
        if adj_arr[S][i] == 1 and visited[i] == 0:
            DFS(i)

# BFS
def BFS(S):
    queue = []
    queue.append(S)
    visited[S] = 1
    while queue:
        t = queue.pop(0)
        print(t, end=' ')
        for i in range(1, N+1):
            if adj_arr[t][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1

N, M, S = map(int, input().split()) # N은 노드의 개수, M은 간선의 개수, S는 시작점
adj_arr = [[0]*(N+1) for _ in range(N+1)]


for i in range(M):
    m1, m2 = map(int, input().split())
    adj_arr[m1][m2] = 1
    adj_arr[m2][m1] = 1 # 방향이 없어서

visited = [0] * (N + 1)
DFS(S)
print()
visited = [0] * (N + 1)
BFS(S)







