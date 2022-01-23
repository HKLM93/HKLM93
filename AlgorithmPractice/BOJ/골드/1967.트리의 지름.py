import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(start, length):
    for i in graph[start]:
        n1, n2 = i
        if distance[n1] == -1:
            distance[n1] = length + n2
            dfs(n1, length + n2)

n = int(input()) # 노드의 개수
graph = [[] for _ in range(n+1)]

# 트리
for _ in range(n-1):
    n1, n2, length = map(int, input().split())
    graph[n1].append([n2, length])
    graph[n2].append([n1, length]) # 방향이 없음

# 1번노드에서 가장 먼 곳 찾기
distance = [-1] * (n+1)
distance[1] = 0
dfs(1, 0)

# 위에서 찾은 노드에 대해서 가장 먼 노드 찾기
start = distance.index(max(distance))
distance = [-1] * (n+1)
distance[start] = 0
dfs(start, 0)

print(max(distance))


