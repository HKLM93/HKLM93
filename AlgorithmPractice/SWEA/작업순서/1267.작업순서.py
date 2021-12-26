import sys
sys.stdin = open('input.txt', 'r')

# 위상 정렬
def topology_sort():
    queue = []

    # 진입차수가 0인 경우 큐에 삽입
    for i in range(1, V+1):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        next = queue.pop(0)
        result.append(next)

        for idx in range(V+1):
            if adj_arr[next][idx] == 1:
                in_degree[idx] -= 1
                if in_degree[idx] == 0:
                    queue.append(idx)

for tc in range(1, 11):
    V, E = map(int, input().split()) # V는 정점의 개수, E는 간선의 개수
    graph = list(map(int, input().split()))
    adj_arr = [[0]*(V+1) for _ in range(V+1)]
    in_degree = [0] * (V+1) # 진입 차수 그래프

    for i in range(E):
        n1, n2 = graph[2*i], graph[2*i+1]
        adj_arr[n1][n2] = 1 # 방향성 존재
        in_degree[n2] += 1 # 진입 차수를 알기 위해

    result = []

    topology_sort()
    ans = ' '.join(list(map(str, result)))

    print('#{} {}'.format(tc, ans))

