import sys
import heapq
input = sys.stdin.readline

# 접근방법: 우선 순위 큐
# 1. 각 가방에 담을 수 있는 모든 보석을 찾을 때 최소힙을 사용
# 2. 각 가방에 넣을 수 있는 보석 중 가장 가치가 큰 보석을 찾을 때 최대힙을 이용

N, K = map(int, input().split()) # N:보석의 개수, K: 가방의 개수

jewerly = []
for _ in range(N):
    weight, value = map(int, input().split())
    heapq.heappush(jewerly, [weight, value])

bags = []
for _ in range(K):
    bags.append(int(input()))
bags.sort()

ans = 0
pick_j = []
for bag in bags:
    while (jewerly and bag >= jewerly[0][0]):
        [weight, value] = heapq.heappop(jewerly)
        heapq.heappush(pick_j, -value)

    if pick_j:
        ans -= heapq.heappop(pick_j)
    elif not jewerly:
        break

print(ans)