import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, target):
    queue = deque()
    queue.append([start, ''])
    # 방문확인
    visited = [0] * 10000
    visited[start] = True

    while queue:
        number, oper = queue.popleft()
        if number == target:
            return oper

        # D
        if not visited[number*2 % 10000]:
            visited[number * 2 % 10000] = True
            queue.append([number*2 % 10000, oper + 'D'])

        # S
        if not visited[(number-1) % 10000]:
            visited[(number - 1) % 10000] = True
            queue.append([(number-1) % 10000, oper + 'S'])

        # L
        if not visited[number % 1000 * 10 + number // 1000]:
            visited[number % 1000 * 10 + number // 1000] = True
            queue.append([number % 1000 * 10 + number // 1000, oper + 'L'])

        # R
        if not visited[number % 10 * 1000 + number // 10]:
            visited[number % 10 * 1000 + number // 10] = True
            queue.append([number % 10 * 1000 + number // 10, oper + 'R'])


T = int(input())
for tc in range(T):
    A, B = map(int, input().split()) # A: 초기 값, B: 최종 값

    print(bfs(A,B))


