import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 50미터에 한 병씩, 한 박스에 맥주는 최대 20개

def bfs(r, c):
    queue = deque()
    queue.append([r, c])
    visited = set() # 편의점 방문 체크
    while queue:
        r, c = queue.popleft()

        # 맥주 한 박스에 1000m를 갈 수 있음으로 거리가 1000m 이내면 도착함
        if abs(r - rock[0]) + abs(c-rock[1]) <= 1000:
            print('happy')
            return

        for i in range(n):
            if i not in visited:
                nr, nc = mart[i]
                # 현재 위치에서 편의점까지의 거리가 1000이내면 갈 수 있음
                if abs(r - nr) + abs(c - nc) <= 1000:
                    queue.append([nr, nc])
                    visited.add(i)
    print('sad')

T = int(input())
for tc in range(T):
    n = int(input()) # n: 맥주를 판매하는 편의점의 개수

    house = list(map(int, input().split()))
    mart = []
    for _ in range(n):
        mart.append(list(map(int, input().split())))
    rock = list(map(int, input().split()))

    bfs(house[0], house[1])


