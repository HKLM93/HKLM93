# import sys
# input = sys.stdin.readline

def count_day(num):
    global ans

    day = N // sum(class_day) * 7 - 7
    left_day = N % sum(class_day) + sum(class_day)

    while left_day:
        left_day -= class_day[num]
        day += 1
        num = (num+1) % 7

    if day < ans:
        ans = day

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    class_day = list(map(int, input().split()))

    ans = 987654321

    for i in range(7):
        if class_day[i]:
            count_day(i)

    print('#{} {}'.format(tc, ans))

