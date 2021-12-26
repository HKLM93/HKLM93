import sys
sys.stdin = open('input.txt', 'r')

def dijkstra(start, adj_arr): #시작 정점과 인접행렬을 받는다
    dist = [987654321] * (N+1)
    visited = [0] * (N+1)
    dist[start] = 0

    for _ in range(N):
        min_idx = -1
        min_value = 987654321

        # 최소값 찾기
        for i in range(N+1):
            if not visited[i] and min_value > dist[i]:
                min_idx = i
                min_value = dist[i]

        visited[min_idx] = 1

        # 갱신할 수 있으면 갱신
        for i in range(N+1):
            if not visited[i] and dist[i] > dist[min_idx] + adj_arr[min_idx][i]:
                dist[i] = dist[min_idx] + adj_arr[min_idx][i]

    return dist

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split()) # N: 집의 개수(정점의 개수) , M: 연결된 길의 개수(간선의 개수), X: 인수네 집 위치

    # x번 집을 기준으로 들어오고(생일파티 오는 것), 나가는 것(자기 집으로 돌아가는 것)을 구하면 된다.
    adj_arr = [[987654321] * (N+1) for _ in range(N+1)] # x번 집으로 올 때
    adj_arr2 = [[987654321] * (N + 1) for _ in range(N + 1)]  # 자기의 집으로 돌아올 때

    for _ in range(M):
        x, y, c = map(int, input().split())
        adj_arr[x][y] = c
        adj_arr2[y][x] = c

    tmp = dijkstra(X, adj_arr)
    tmp2 = dijkstra(X, adj_arr2)

    ans = []
    for i in range(1, N+1):
        ans.append(tmp[i] + tmp2[i])

    print('#{} {}'.format(tc, max(ans)))

