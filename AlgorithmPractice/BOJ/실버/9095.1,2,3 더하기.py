import sys
input = sys.stdin.readline

# 점화식 규칙: dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

T = int(input())

# n=1, n=2, n=3일 때의 개수
dp = [1, 2, 4]

tmp_list = []

for _ in range(T):
    tmp_list.append((int(input())))

# 3까지의 값은 이미 존재하니 3부터 시작
for i in range(3, max(tmp_list)):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

for i in tmp_list:
    print(dp[i-1])


