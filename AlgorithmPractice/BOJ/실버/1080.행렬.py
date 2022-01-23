import sys
input = sys.stdin.readline

# 3x3 크기 부분의 행렬에 있는 모든 원소 뒤집기
def change(r, c):
    for i in range(r, r+3):
        for j in range(c, c+3):
            arr_A[i][j] = 1 - arr_A[i][j]


N, M = map(int, input().split()) # N: 행, M: 열
arr_A = [list(map(int, input().strip())) for _ in range(N)] # A행렬
arr_B = [list(map(int, input().strip())) for _ in range(N)] # B행렬

flag = 0 # 변환할 수 있는지 확인
cnt = 0 # 변환 횟수
for i in range(N-2):
    for j in range(M-2):
        if arr_A[i][j] != arr_B[i][j]:
            change(i, j)
            cnt += 1

for i in range(N):
    for j in range(M):
        # 변환이 불가능하면
        if arr_A[i][j] != arr_B[i][j]:
            flag = 1
            break

if flag == 1:
    print(-1)
else:
    print(cnt)




