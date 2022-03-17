import sys
sys.stdin = open('sample_input.txt', 'r')

# 충전회수 구하기
def charge(idx):
    global cnt, result

    # 도착하면 충전횟수의 최소값 구하기
    if idx >= len(arr):
        if result >= cnt:
            result = cnt
        return

    # 가지치기
    if result <= cnt:
        return

    # 충전으로 최대로 갈 수 있는 정류장부터 경우의 수를 따진다.
    for i in range(idx + arr[idx], idx, -1): # for문인 이유는 충전량을 했음에도 반드시 그만큼 갈 필요가 없기 때문
        cnt += 1 # 다음 정류장에 도착했으니 충전
        charge(i)
        cnt -= 1 # 다시 돌아왔으니 충전 횟수를 빼준다.

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    N = arr[0]

    result = 987654321
    cnt = 0 # 충전 횟수

    charge(1)

    print('#{} {}'.format(tc, result-1)) # 출발지점 충전은 빼줘야 한다.


###############################################################################
# 교수님 답안

# idx: 현재 내가 있는 버스 정류장 번호
# e: 잔여 배터리
# c: 지금까지의 교환횟수
# def move(idx, e, c):
#     global ans
#     if idx == bus_stop[0]:
#         if ans > c:
#             ans = c
#         return
#     else:
#         # 배터리를 교체하지 않고 내려보내기
#         if e > 0:
#             move(idx + 1, e - 1, c)
#         # 배터리를 교체하고 내려보내기
#         if c < ans: # 가지치기
#             move(idx + 1, bus_stop[idx] -1 , c+1)
#
# T = int(input())
# for tc in range(1, T+1):
#     bus_stop = list(map(int, input().split()))
#
#     ans = 987654321
#
#     move(2, bus_stop[1] - 1, 0)
#
#     print('#{} {}'.format(tc, ans))


