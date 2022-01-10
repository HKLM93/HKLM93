import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set()
for _ in range(N):
    S.add(input().strip())

check = []
for _ in range(M):
    check.append(input().strip())

cnt = 0

for i in check:
    if i in S:
        cnt += 1

print(cnt)