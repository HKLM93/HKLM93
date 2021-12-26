import sys
sys.stdin = open('sample_input.txt', 'r')

def dfs(node, cnt): # node는 시작 노드, cnt는 거리
    global ans
    # 방문 표시
    visited[node] = 1

    if ans < cnt:
        ans = cnt

    for i in adj_list[node]:
        if visited[i] == 0:
            dfs(i, cnt+1)
            # 초기화
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N은 정점의 개수, M은 간선의 개수
    # 인접 리스트
    adj_list = [[] for _ in range(N+1)]# 0번 인덱스는 사용하지 않음

    for i in range(M):
        n1, n2 = map(int, input().split())
        adj_list[n1].append(n2)
        adj_list[n2].append(n1) # 방향이 없는 그래프

    ans = 0

    # 1번 노드 부터 탐색
    for i in range(1, N+1):
        visited = [0] * (N + 1)
        dfs(i, 1)

    print('#{} {}'.format(tc, ans))
