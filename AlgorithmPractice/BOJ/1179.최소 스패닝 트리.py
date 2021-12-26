import sys
input = sys.stdin.readline

def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])

def union(x, y):
    if find_set(x) > find_set(y):
        parent[find_set(x)] = find_set(y)
    else:
        parent[find_set(y)] = find_set(x)

def kruskal(graph):
    global ans

    for node in graph:
        x, y, w = node[0], node[1], node[2]

        if find_set(x) != find_set(y):
            union(x, y)
            ans += w


V, E = map(int, input().split()) # V는 정점, E는 간선
graph = []

parent = [0] * (V+1)
for i in range(1, V+1):
    parent[i] = i

for _ in range(E):
    n1, n2, w = map(int, input().split())
    graph.append([n1, n2, w])

# 크루스칼은 가중치를 기준으로 오름차순 정렬해야 한다.
graph.sort(key=lambda x : x[2])

ans = 0

kruskal(graph)

print(ans)


