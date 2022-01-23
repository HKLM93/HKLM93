import sys
import heapq
input = sys.stdin.readline

# 접근방법: 힙큐 사용(최소 힙) - 합이 가장 작은 큐만 뽑아 줌

N = int(input())
cards = []

for _ in range(N):
    heapq.heappush(cards, int(input()))

if len(cards) == 1:
    print(0)

else:
    ans = 0
    while len(cards) > 1:
        result = heapq.heappop(cards) + heapq.heappop(cards)
        ans += result
        heapq.heappush(cards, result)
    print(ans)

