import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N: 세로크기, M: 가로크기
arr = [list(input().strip()) for _ in range(N)]
cnt = 0

# 가로판자 개수 세기
for i in range(N):
    if arr[i][0] == '-':
        cnt += 1
        for j in range(1, M-1):
            if arr[i][j] == '|' and arr[i][j+1] == '-':
                cnt += 1
    else:
        for j in range(M-1):
            if arr[i][j] == '|' and arr[i][j+1] == '-':
                cnt += 1

# 세로판자 개수 세기
for j in range(M):
    if arr[0][j] == '|':
        cnt += 1
        for i in range(1, N-1):
            if arr[i][j] == '-' and arr[i+1][j] == '|':
                cnt += 1
    else:
        for i in range(N-1):
            if arr[i][j] == '-' and arr[i+1][j] == '|':
                cnt += 1

print(cnt)


