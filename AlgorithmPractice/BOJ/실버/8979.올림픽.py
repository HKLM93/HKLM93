import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # N: 참여 국가 수, K: 등수를 알고 싶은 국가
olimpic = []
for _ in range(N):
    nation, gold, silver, bronze = map(int, input().split())
    olimpic.append([nation, gold, silver, bronze])

olimpic.sort(key= lambda x: (-x[1], -x[2], -x[3]))

# 해당 등수의 국가 구하기
for i in range(N):
    if olimpic[i][0] == K:
        index = i

# 개수가 같은 경우 등수 구하기
for i in range(N):
    if olimpic[index][1:] == olimpic[i][1:]:
        print(i+1)
        break