import sys
sys.stdin = open('sample_input.txt', 'r')

# DFS 함수
def DFS(S, G, V):
    visited = [0] * (V+1)
    stack = []
    i = S # 현재 방문한 노드
    visited[i] = 1

    while True:
        for w in range(1, V+1):
            # 도착
            if visited[G] == 1:
                return 1
            if adj_arr[i][w] == 1 and visited[w] == 0:
                stack.append(i) # 방문경로 저장
                i = w # 새 방문지 이동
                visited[i] = 1
                break
        # 다음 노드가 없는 경우
        else:
            if stack:
                i = stack.pop() # 지나온 노드가 남아있는 경우
            else:
                return 0 # 지나온 노드가 남아있지 않는 경우
    return



T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    adj_arr = [[0] * (V+1) for _ in range(V+1)]

    for i in range(E):
        st, ed = map(int, input().split())
        adj_arr[st][ed] = 1 # 방향성이 있기 때문

    S, G = map(int, input().split())

    ans = DFS(S, G, V)

    print('#{} {}'.format(tc, ans))
