import sys
sys.stdin = open('input.txt', 'r')

def powerset(num, height):
    global ans
    # 선반보다 높이가 높아졌을 때
    if height >= B:
        result = height - B # 선반과 직원들의 키를 빼줌
        # 최소값 구하기
        if result < ans:
            ans = result

    if num == N:
        return

    # 직원의 키를 포함시키지 않는 경우
    powerset(num + 1, height)
    # 직원의 키를 포함시키는 경우
    powerset(num + 1, height+H[num])

    # -> 시간 초과 ㅠㅠ
    # for i in range(N+1):
    #     if not visited[i]:
    #         visited[i] = 1
    #         powerset(num+1, height + H[i])
    #         visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split()) # N은 점원의 수, B는 선반의 높이
    H = list(map(int, input().split())) # 점원들의 키
    # visited = [0] * (N+1)

    ans = 987654321

    powerset(0, 0)

    print('#{} {}'.format(tc, ans))


#############################################
# 1. 비트 마스킹
# for i in range(0, (1 << N)):
     # 초기화 필요
#     for j in range(0, N):
#         if i & (1 << j):
            # 직원들의 키의 합
        # 비교

# 접근 방법
# 직원을 탑으로 쌓았을 때와 안 쌓았을 때로 나누어서 높이를 쌓아간다.


