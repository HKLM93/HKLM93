import sys
input = sys.stdin.readline

# 접근방법: B에서 A로 가는 횟수를 찾자

A, B = map(int, input().split())

ans = 1
while A < B:
    # B를 2로 나누어줌
    if (B % 2) == 0:
        B = B//2
    # B의 마지막에 1을 떼어줌
    elif str(B)[-1] == '1':
        B = int(str(B)[:-1])
    # 다른 못찾는 경우
    else:
        break
    ans += 1

if A == B:
    print(ans)
else:
    print(-1)

## 정수로 접근하니 시간초과.... 
