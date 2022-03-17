import sys
sys.stdin = open('sample_input.txt', 'r')

def BFS(S, V): # 시작점 S, 정점의 개수 V
    global result
    visited = [0] *(V+1)
    distance = [0]*(V+1)
    queue = []
    queue.append(S)
    visited[S] = 1
    while queue:
        t = queue.pop(0)
        for i in range(1, V+1):
            if adj[t][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[i] + 1
                distance[i] = distance[t] + 1 # 거리 계산
                if i == G: # 도착하면 검색 종료(최단거리라서)
                    result = distance[i]
                    return
    return 0 # S,G가 서로 연결이 안 되어 있을 때

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)] # 인접행렬(0번 노드는 안 사용)

    for i in range(E):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1
        adj[n2][n1] = 1 # 방향이 없는 그래프
    S, G = map(int, input().split())
    result = 0

    BFS(S, V)

    print('#{} {}'.format(tc, result))



