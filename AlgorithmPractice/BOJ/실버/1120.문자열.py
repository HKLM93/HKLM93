import sys
input = sys.stdin.readline

A, B = list(input().split())
ans = []

for i in range(len(B)-len(A) + 1):
    cnt = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            cnt += 1
    ans.append(cnt)

print(min(ans))

