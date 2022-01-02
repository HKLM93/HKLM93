import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N: 듣도 못한 사람의 수, M: 보도 못한 사람의 수

########################################3
# 나의 답

no_listen = []
for _ in range(N):
    no_listen.append(input().strip())
no_listen.sort()

no_see = []
for _ in range(M):
    no_see.append(input().strip())
no_see.sort()

cnt = 0
ans = []
for i in no_listen:
    for j in no_see:
        if i == j:
            cnt += 1
            ans.append(i)

print(cnt)
for k in ans:
    print(k)

######################################3
# 모범답안(시간을 줄이기 위함) - set의 교집합 활용
no_listen = set()
for _ in range(N):
    no_listen.add(input().strip())

no_see = set()
for _ in range(M):
    no_see.add(input().strip())

ans = sorted(list(no_see & no_listen))
print(len(ans))

for i in ans:
    print(i)




