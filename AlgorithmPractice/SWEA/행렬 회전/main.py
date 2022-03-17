import sys
sys.stdin = open('input (1).txt', 'r')

# 행렬의 90도 회전
def rotate(arr):
    empty_list = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            empty_list[j][N-1-i] = arr[i][j]
    return empty_list

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 행렬의 90도 회전
    rotate_90 = rotate(arr)

    # 행렬의 180도 회전
    # 90도 회전한 행렬을 다시 90도 회전시키면 됨
    rotate_180 = rotate(rotate_90)

    # 행렬의 270도 회전
    # 180도 회전한 행렬을 다시 90도 회전시키면 됨
    rotate_270 = rotate(rotate_180)

    print('#{}'.format(tc))
    # 구한 리스트를 문자로 바꾸어 주어야 함
    for i in range(N):
        print(''.join(map(str, rotate_90[i])), ''.join(map(str, rotate_180[i])), ''.join(map(str, rotate_270[i])))






