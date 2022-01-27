import sys
input = sys.stdin.readline

# 동서북남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 주사위를 굴렸을 때 바뀌는 부분만 바꿔준다.
# dice[1]은 밑면, dice[6]은 윗면이다.
def move(function):
    if function == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif function == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif function == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    elif function == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]

N, M, x, y, K = map(int, input().split()) # N:세로 크기, M: 가로 크기, x:주사위를 놓은 곳의 행, y: 주사위를 놓은 곳의 열, K: 명령의 개수
arr = [list(map(int, input().split())) for _ in range(N)]
oper = list(map(int, input().split())) # 동쪽: 1, 서쪽: 2, 북쪽: 3, 남쪽: 4

dice = [0, 0, 0, 0, 0, 0, 0]
ans = []
for i in range(K):
    dir = oper[i] - 1
    nx = x + dx[dir]
    ny = y + dy[dir]

    if 0 <= nx < N and 0 <= ny < M:
        move(oper[i])

        if arr[nx][ny] == 0:
            arr[nx][ny] = dice[1]
        else:
            dice[1] = arr[nx][ny]
            arr[nx][ny] = 0
        x, y = nx, ny
        print(dice[6])





