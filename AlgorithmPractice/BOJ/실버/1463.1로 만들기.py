import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)

for i in range(2, N+1): # 첫번째는 1을 빼고 시작하기 때문
    dp[i] = dp[i-1] + 1

    if i%2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1 # 1을 더하는 것은 계산한 횟수를 저장하기 때문

    if i%3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1

print(dp[N])
