import sys
from collections import deque
input = sys.stdin.readline

# 위상정렬
def bfs():
    global graph

    while queue:
        curr = queue.popleft()
        answer.append(curr)

        for next in graph[curr]:
            line[next] -= 1
            if line[next] == 0:
                queue.append(next)

N, M = map(int, input().split()) # N은 학생의 수, M은 키를 비교한 횟수
graph = [[] for _ in range(N+1)]
line = [0] * (N+1)
answer = []

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    line[n2] += 1

queue = deque()
for i in range(1, N+1):
    if line[i] == 0:
        queue.append(i)
bfs()

for ans in answer:
    print(ans, end= ' ')