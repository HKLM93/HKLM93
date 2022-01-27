import sys
input = sys.stdin.readline

N = int(input().strip())
score = []
for _ in range(N):
    score.append(int(input().strip()))

idx = len(score) -1
cnt = 0
while idx > 0:
    if score[idx] <= score[idx-1]:
        score[idx-1] -= 1
        cnt += 1
    else:
        idx -= 1

print(cnt)