import sys
input = sys.stdin.readline

# 다를 때마다 바꿔주고 이 횟수를 반으로 나누면 된다.
S = input().strip()
cnt = 0

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        cnt += 1

print((cnt+1) // 2)

