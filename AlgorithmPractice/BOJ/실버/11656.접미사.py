import sys
input = sys.stdin.readline

S = input().strip()

idx = 0
ans = []
while idx < len(S):
    ans.append(S[idx:len(S)])
    idx += 1

ans.sort()

for i in ans:
    print(i)
