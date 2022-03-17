import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def bfs(start): # 시작점, 최종적으로 연락을 받는 사람의 번호
    global ans

    queue = deque()
    queue.append(start)

    visited = [0] * (N+1)
    visited[S] = 1

    while queue:
        curr = queue.popleft()

        for next in range(1, N+1):
            if adj_list[curr][next] and visited[next] == 0:
                queue.append(next)
                visited[next] = 1
                distance[next] = distance[curr] + 1 # 거리 1 더하기

for tc in range(1, 11):
    L, S = map(int, input().split()) # L은 입력받는 데이터의 길이, S는 시작점
    V = L // 2 # V는 정점의 개수
    connection = list(map(int, input().split())) # 연결상태
    N = max(connection) # 입력값 리스트 중 가장 높은 값을 최대값으로 설정하기 위해
    adj_list = [[0] * (N+1) for _ in range(N+1)]

    for i in range(V):
        n1, n2 = connection[2*i], connection[2*i+1]
        adj_list[n1][n2] = 1 # 방향성이 존재

    distance = [0] * (N + 1) # 거리를 담을 리스트

    # 너비 탐색
    bfs(S)

    result = [] # 마지막에 연락할 사람들을 담을 리스트
    max_d = distance[0] # 0번 인덱스는 사용하지 않아 0이기 때문에 초기값으로 설정 가능
    for idx in range(1, len(distance)):
        if max_d <= distance[idx]:
            max_d = distance[idx]
            result.append(idx) # 최대값들을 담아 줌

    print('#{} {}'.format(tc, max(result)))