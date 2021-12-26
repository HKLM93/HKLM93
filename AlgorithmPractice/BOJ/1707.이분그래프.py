import sys
from collections import deque
input = sys.stdin.readline

### 1. dfs 풀이
# def dfs(v, visit):
#     visited[v] = visit # 방문 체크
#
#     for i in graph[v]:
#         if visited[i] == 0:
#             if not dfs(i, -visit): # 다른 그룹이라 방문 체크를 -1로 해줌
#                 return False
#         elif visited[i] == visited[v]:
#             return False
#     return True
#
# K = int(input())
# for tc in range(K):
#     V, E = map(int, input().split())
#     graph = [[] for _ in range(V+1)]
#     visited = [0] * (V+1)
#
#     for _ in range(E):
#         n1, n2 = map(int, input().split())
#         graph[n1].append(n2)
#         graph[n2].append(n1) # 방향이 없음
#
#     flag = True
#
#     for i in range(1, V+1):
#         if visited[i] == 0:
#             flag = dfs(i, 1)
#
#     if flag:
#         print('YES')
#     else:
#         print('NO')

############################################
# 2. bfs풀이

def bfs(start):
    visited[start] = 1
    queue = deque()
    queue.append(start)

    while queue:
        now = queue.popleft()

        for next in graph[now]:
            # 방문하지 않았으면
            if visited[next] == 0:
                visited[next] = -visited[now] # 현재 노드와 다른 그룹 지정(이분 그래프)
                queue.append(next)
            # 방문한 경우, 동일 그룹에 속하면
            else:
                if visited[next] == visited[now]:
                    # 이분 그래프가 아니다
                    return False
    return True

K = int(input())
for tc in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    for _ in range(E):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1) # 방향이 없음

    flag = True

    for i in range(1, V+1):
        if visited[i] == 0:
            if not bfs(i):
                flag = False
                break

    if flag:
        print('YES')
    else:
        print('NO')

