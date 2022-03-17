import sys
input = sys.stdin.readline

dr = [-1, 0, 1]
dc = [1, 1, 1]

def pipe(i, j):
    field[i][j] = 'x'
    if j == C - 1:
        return True

    for k in range(3):
        ni = i + dr[k]
        nj = j + dc[k]

        if 0 <= ni < R and  0 <= nj < C and field[ni][nj] == '.':
            if pipe(ni, nj):
                return True
    return False

R, C = map(int, input().split())
field = [list(input().strip()) for _ in range(R)]

ans = 0
for i in range(R):
    if pipe(i, 0):
        ans += 1

print(ans)