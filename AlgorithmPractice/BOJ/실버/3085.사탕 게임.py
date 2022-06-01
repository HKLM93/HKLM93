import sys
input = sys.stdin.readline

def check(arr):
    n = len(arr)
    result = 1

    for i in range(n):
        # 열 순회로 체크
        cnt = 1
        for j in range(1, n):
            # 이전과 같다면 사탕 먹기
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            # 이전과 다르면 사탕 안 먹음
            else:
                cnt = 1
            # 비교해서 최대로 먹을 수 있는 수 갱신
            if cnt > result:
                result = cnt
        # 행순회로 체크
        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1

            if cnt > result:
                result = cnt
    return result




N = int(input())
arr = [list(input()) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(N):
        # 행바꾸기
        if i+1 < N:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

            tmp = check(arr)
            if tmp > ans:
                ans = tmp

            # 바꿨던 부분 되돌려 놓기
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
        if j+1 < N:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

            tmp = check(arr)
            if tmp > ans:
                ans = tmp

            # 바꿨던 부분 되돌려 놓기
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
print(ans)