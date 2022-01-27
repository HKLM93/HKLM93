import sys
input = sys.stdin.readline


N = int(input().strip()) # N: 로프의 개수
weights = []
for _ in range(N):
    weights.append(int(input().strip()))

weights.sort(reverse=True)
ans = []
for i in range(N):
    ans.append(weights[i]*(i+1))

print(max(ans))


