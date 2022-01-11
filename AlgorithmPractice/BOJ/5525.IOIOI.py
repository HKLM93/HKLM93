import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

cnt = 0 # Pn과 같은 모양인지 확인하기 위함
ans = 0 # Pn과 같은 것의 개수
i = 1
while i < M-1:
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] =='I':
        cnt += 1
        if cnt == N:
            cnt -= 1
            ans += 1
        i += 1
    else:
        cnt = 0
    i += 1

print(ans)


