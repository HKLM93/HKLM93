import sys
input = sys.stdin.readline

def dfs(node):

    for n in graph[node]:
        if visited[n] == 0:
            visited[n] = visited[node] + 1
            dfs(n)

n = int(input()) # 사람의 수
target = list(map(int, input().split())) # 시작점과 도착지점
m = int(input()) # 부모 자식들 간의 관계의 수

graph = [[] for _ in range(n+1)] # 인접리스트
for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1) # 방향성 없음

visited = [0]*(n+1)

dfs(target[0])

if visited[target[1]] > 0:
    # 촌수가 연결되면
    print(visited[target[1]])
else:
    # 촌수가 연결 안 되면
    print(-1)

