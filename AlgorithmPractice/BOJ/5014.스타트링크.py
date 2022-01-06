import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    global cnt
    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        floor = queue.popleft()

        if floor == G:
            return count[floor]

        for next in (floor + U, floor - D):
            if 0 < next <= F and visited[next] == 0:
                visited[next] = 1
                count[next] = count[floor] + 1
                queue.append(next)

    if count[G] == 0:
        return 'use the stairs'

# F: 건물의 총 층수, S: 현재 층, G: 스타트링크가 있는 층, U: 올라갈 수 있는 층수, D: 내려갈 수 있는 층수
F, S, G, U, D = map(int, input().split())

visited = [0] * (F+1)
count = [0] * (F+1)
cnt = 0

print(bfs(S))

