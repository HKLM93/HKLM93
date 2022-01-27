import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):

    VPS = list(input().strip())
    cnt = 0

    for word in VPS:
        if word == '(':
            cnt += 1
        elif word == ')':
            cnt -= 1
        if cnt < 0:
            print('NO')
            break

    if cnt > 0:
        print('NO')
    elif cnt == 0:
        print('YES')



