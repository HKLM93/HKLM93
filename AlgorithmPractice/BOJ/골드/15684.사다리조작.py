import sys
input = sys.stdin.readline

def check():
    for start in range(N): # 1번부터 N번 세로선까지 검사
        k = start # k는 이동하는 가로선
        for j in range(H): # 가로선 이동
            if visited[j][k]: # 가로선이 존재한다면
                k += 1 # 가로선 오른쪽으로 한 칸 이동
            elif k >0 and visited[j][k-1]: # 가로선이 왼쪽에 존재한다면
                k -= 1 # 가로선 왼쪽으로 한 칸 이동
        if k != start: # 가장 하단까지 왔는데 k가 start랑 같지 않으면 정상 도착하지 않은 것
            return False
    return True

def dfs(cnt, r, c):
    global ans

    if check(): # i번째에서 출발해서 i번째에 도착하는지 확인
        ans = min(ans, cnt)
        return

    # 가지치기(자기 번호에 도착하지 않거나 최소값이 아닐 경우)
    elif cnt == 3 or ans <= cnt:
        return

    # 행
    for i in range(r, H):
        # 가로선을 먼저 탐색
        if i == r: # 행이 변경되기 전에는 가로선 계속 탐색
            k = c
        else: # 행이 변경될 경우 가로선 처음부터 탐색
            k = 0
        # 세로선 탐색
        for j in range(k, N-1):
            if visited[i][j] == 0 and visited[i][j+1] == 0: # 가로선을 놨을 때 오른쪽에 다른 가로선이 없을 때
                if j > 0 and visited[i][j-1]:# 가로선을 놨을 때 왼쪽에 다른 가로선이 없을 때
                    continue
                visited[i][j] = 1 # 가로선 놓기
                dfs(cnt+1, i, j+2) # 가로선은 연속되면 안 되서 2증가
                visited[i][j] = 0 # 가로선 초기화

N, M, H = map(int, input().split()) # N: 세로선의 개수, M: 가로선의 개수, H: 각각의 세로선마다 가로선을 놓을 수 있는 위치(점선의 개수)
visited = [[0] * N for _ in range(H)] # 방문체크

if M == 0: # M이 0이면 그냥 바로 내려옴
    print(0)
    exit(0)

for _ in range(M):
    a, b = map(int, input().split()) # a: 가로선의 번호, b: 연결된 세로선(b와 b+1)
    visited[a-1][b-1] = 1

ans = 4 # 3보다 큰 값은 -1을 출력해야 함으로 초기값을 4로 줌
dfs(0, 0, 0)
if ans < 4:
    print(ans)
else:
    print(-1)