import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

player = []
for i in range(N):
    player.append(i)
team = list(combinations(player, N//2))

ans = 987654321
# 조합의 절반이 A팀, 나머지 절반이 B팀이다(알아서 오름차순 정렬을 해주기 때문)
for i in range(len(team)):
    # A팀
    A_team = team[i]
    A = 0 # A팀의 능력치
    for j in range(N//2):
        member = A_team[j]
        for k in A_team:
            A += arr[member][k]
    # B팀
    B_team = team[-i-1]
    B = 0 # B팀의 능력치
    for j in range(N//2):
        member = B_team[j]
        for k in B_team:
            B += arr[member][k]

    ans = min(ans, abs(A-B))

print(ans)

