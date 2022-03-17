import sys

def DFS(S):
    global cnt
    visited[S] = 1
    for i in range(1, V+1):
        if adj_arr[S][i] == 1 and visited[i] == 0:
            DFS(i)
            cnt += 1

V = int(input()) # 노드의 개수
E = int(input()) # 간선의 개수

adj_arr = [[0]*(V+1) for _ in range(V+1)]
visited = [0]*(V+1)

for i in range(E):
    n1, n2 = map(int, input().split())
    adj_arr[n1][n2] = 1
    adj_arr[n2][n1] = 1 # 방향성이 없음

cnt = 0

DFS(1)
print(cnt)