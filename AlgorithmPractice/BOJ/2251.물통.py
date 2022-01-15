import sys
from collections import deque
input = sys.stdin.readline

# 물을 따를 수 있는 모든 경우의 수를 계산
def bfs():
    while queue:
        x, y, z = queue.popleft()
        if check[x][y] == 1:
            continue

        check[x][y] = 1

        if x == 0:
            ans[z] = 1

        if x + y > B:
            queue.append([x + y - B, B, z])
        else:
            queue.append([0, x + y, z])

        if x + z > C:
            queue.append([x + z - C, y, C])
        else:
            queue.append([0, y, x + z])

        if y + x > A:
            queue.append([A, y + x - A, z])
        else:
            queue.append([y + x, 0, z])

        if y + z > C:
            queue.append([x, y + z - C, C])
        else:
            queue.append([x, 0, y + z])

        if z + x > A:
            queue.append([A, y, z + x - A])
        else:
            queue.append([z + x, y, 0])

        if z + y > B:
            queue.append([x, B, z + y - B])
        else:
            queue.append([x, z + y, 0])

A, B, C = map(int, input().split())
check = [[0] * 201 for i in range(201)] # A, B, C 모두 200이하
ans = [0] * 201
queue = deque()
queue.append([0, 0, C])
bfs()

for i in range(201):
    if ans[i]:
        print(i, end =' ')