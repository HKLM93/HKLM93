import sys
sys.stdin = open('sample_input.txt', 'r')

def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])

def union(x, y):
    a = find_set(x)
    b = find_set(y)

    # 가중치 중 최소값을 구해야 한다
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

# 크루스칼 알고리즘
def Kruskal(graph):
    global ans

    for node in graph:
        x, y, w = node[0], node[1], node[2]
        # 부모가 다른 경우만(싸이클이 안 생기는 경우)
        if find_set(x) != find_set(y):
            # 부모를 병합
            union(x, y)
            ans += w

    # while문일 때
    # cnt = 0
    # idx = 0

    # while cnt < V:
    #     n1 = graph[idx][0]
    #     n2 = graph[idx][1]
    #
    #     if find_set(x) != find_set(y):
    #         union(x, y)
    #         cnt += 1
    #         ans += graph[idx][2]
    #     idx += 1

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    parent = [0] * (V+1)
    for i in range(1, V+1):
        parent[i] = i

    # 가중치를 기준으로 오름차순 정렬해주기
    tmp = []
    for i in range(E):
        n1, n2, w = map(int, input().split())
        tmp.append([n1, n2, w])
    graph = sorted(tmp, key = lambda x: x[2])

    ans = 0

    Kruskal(graph)

    print('#{} {}'.format(tc, ans))

####################################################3
# prim 알고리즘(아무 정점에서 출발해도 답이 같다)

# def prim():
#     key = [987654321] (V*1)
#     visited = [0] * (V+1)
#     key[0] = 0
#
#     for _ in range(V):
#         min_idx = -1
#         min_value = 987654321
#
#         # 최소값 찾기
#         for i in range(V+1):
#             if not visited[i] and key[i] < min_value:
#                 min_idx = i
#                 min_value = key[i]
#         visited[min_idx] = 1
#
#         # 갱신할 수 있으면 전부 갱신
#         for i in range(V+1):
#             if not visited[i] and adj_arr[min_idx][i] < key[i]:
#                 key[i] = adj_arr[min_idx][i]
#
#     return sum(key)
#
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#
#     adj_arr = [[987654321] * (V+1) for _ in range(V+1)]
#
#     for i in range(E):
#         n1, n2, w = map(int, input().split())
#         adj_arr[n1][n2] = adj_arr[n2][n1] = w
#
#     ans = 0
#
#     print(prim())

##########################################################
# heqpq를 활용한 MST
#
# import heapq
#
# def prim():
    # visited = [0] * (V+1)
    # heap = [] # 큐로 선언해도 상관 없다
    # 가중치와 정점을 넣음
    # heapq.heappush(heap, (0, 0))
    #
    # while heap:
    #     w, v = heapq.heappop(heap)
    #     if not visited[v]:
    #         ans += w
    #         visited[v] = 1
    #
    #         for idx, weight in adj_arr[v]:
    #             if not visited[idx]:
    #                 heapq.heappush(heap, (weight, idx))
    # return ans

# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#
#     adj_arr = [[] for _ in range(V+1)]
#     for i in range(E):
#         n1, n2, w = map(int, input().split())
#         adj_arr[n1].append((n2, w))
#         adj_arr[n2].append((n1, w))
# print(prim())