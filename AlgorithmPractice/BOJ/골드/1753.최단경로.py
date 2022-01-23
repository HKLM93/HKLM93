import sys
import heapq

# 방향이 있고 가중치를 가지고 있는 그래프에서의 단일 시작점 최단 경로는 데이크스트라(다익스트라) 알고리즘을 사용하는 것이 좋다. 단, 가중치는 음수가 아니여야 한다.
# heap은 우선순위가 있는 queue

def dijkstra(S):
    queue = []
    heapq.heappush(queue, (0, S))
    distance[S] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in adj[now]:
            next_w = dist + i[1]

            if next_w < distance[i[0]]:
                distance[i[0]] = next_w
                heapq.heappush(queue, (next_w, i[0]))

V, E = map(int, sys.stdin.readline().split()) # V는 정점의 개수, E는 간선의 개수
K = int(sys.stdin.readline()) # K는 시작
INF = int(1e9) # 무한대를 나타내는 의미

adj = [[] for _ in range(V+1)]
distance = [INF] * (V+1) # 거리를 계산하기 위함

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split()) # u는 출발노드, v는 다음노드, w는 가중치(비용)
    adj[u].append((v, w))

dijkstra(K)

for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])

# heap을 안 배워서 그런지 잘 모르겠다 ㅠ

