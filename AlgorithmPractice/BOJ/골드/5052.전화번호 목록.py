import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    phone_number = []
    flag = True

    for _ in range(N):
        phone_number.append(input().strip())

    phone_number.sort()

    for i in range(N-1):
        long = len(phone_number[i])

        if phone_number[i] == phone_number[i+1][:long]:
            flag = False
            break

    if flag:
        print('YES')
    else:
        print('NO')



