import sys
from itertools import combinations # 조합을 뽑아내는 라이브러리
input = sys.stdin.readline


N, M = map(int, input().split()) # N: 도시크기, M: 치킨집의 최대 수
area = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

for i in range(N):
    for j in range(N):
        if area[i][j] == 1:
            house.append([i, j])
        elif area[i][j] == 2:
            chicken.append([i, j])

pick_ch = list(combinations(chicken, M)) # 치킨집 중 M개를 고름
ans = [0] * len(pick_ch)

# 집과 치킨집에 대한 거리를 계산하여 최소거리를 구하고 더한다.
for i in house:
    for j in range(len(pick_ch)):
        result = 987654321
        for k in pick_ch[j]:
            tmp = abs(i[0]-k[0]) + abs(i[1]-k[1])
            result = min(result, tmp)
        ans[j] += result
print(min(ans))








