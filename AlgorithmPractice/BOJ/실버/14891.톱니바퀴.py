import sys
from collections import deque
input = sys.stdin.readline

circle = [deque(map(int, input().strip())) for _ in range(4)]
opers = deque(list(map(int, input().split())) for _ in range(int(input())))

while opers:  # 명령어가 남아 있으면 반복문 실행
    num, direct = opers.popleft()
    num -= 1  # 0 index
    tmp_2 = circle[num][2]  # 비교 대상 백업
    tmp_6 = circle[num][6]  # 비교 대상 백업
    circle[num].rotate(direct)  # 일단 시작 톱니 돌려주기
    tmp_direct = direct

    # 시작 톱니 왼쪽 방향
    direct = tmp_direct
    for i in range(num - 1, 0 - 1, -1):
        if circle[i][2] != tmp_6:  # 서로 다른 극인 경우
            tmp_6 = circle[i][6]
            circle[i].rotate(direct * -1)
            direct *= -1
        else:
            break

    # 시작 톱니 오른쪽 방향
    direct = tmp_direct
    for i in range(num + 1, 4):
        if circle[i][6] != tmp_2:  # 서로 다른 극인 경우
            tmp_2 = circle[i][2]
            circle[i].rotate(direct * -1)
            direct *= -1
        else:
            break

ans = 0
for i in range(4):
    if circle[i][0] == 1:
        ans += (2 ** i)
print(ans)




