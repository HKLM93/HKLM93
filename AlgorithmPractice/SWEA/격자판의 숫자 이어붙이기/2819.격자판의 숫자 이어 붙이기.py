import sys
sys.stdin = open('sample_input.txt', 'r')

# 동서남북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

# DFS를 통한 숫자만들기
def make_num(r, c, num):
    if len(num) == 7:
        # 중복처리
        # if num not in ans:
        #     ans.append(num)
        ans.add(num)
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= 4 or nc < 0 or nc >= 4:
            continue

        make_num(nr, nc, num + arr[nr][nc])

T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]

    # ans = []
    ans = set()

    # 만든 문자를 계속 가지고 가기
    for i in range(4):
        for j in range(4):
            make_num(i, j, arr[i][j])

    print('#{} {}'.format(tc, len(ans)))