import sys
input = sys.stdin.readline

board = input().strip()
tmp = board.replace('XXXX', 'AAAA')
ans = tmp.replace('XX', 'BB')

if 'X' in ans:
    print(-1)
else:
    print(ans)