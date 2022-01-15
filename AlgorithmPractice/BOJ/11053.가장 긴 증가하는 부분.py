import sys
input = sys.stdin.readline

A = int(input()) # 수열의 크기
A_list = list(map(int, input().split()))
dp = [0] * A

for i in range(A):
    for j in range(A):
        if A_list[i] > A_list[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))


