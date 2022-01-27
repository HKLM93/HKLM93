import sys
input = sys.stdin.readline

stair = int(input()) # 계단의 개수
scores = [0] + [int(input()) for _ in range(stair)] + [0]  # 점수

dp = [0] * (stair+2)
dp[1] = scores[1]
dp[2] = dp[1] + scores[2]

for i in range(3, stair+1):
    dp[i] = max(dp[i-2], dp[i-3] + scores[i-1]) + scores[i]

print(dp[stair])