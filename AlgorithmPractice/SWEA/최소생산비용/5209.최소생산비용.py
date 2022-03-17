import sys
sys.stdin = open('sample_input.txt', 'r')

# 1. visited 활용
def min_v(r, result): # 행을 살펴보면서 생산비용을 더함
    global ans

    # 행 끝까지 훑었으면
    if r == N:
        if result < ans:
            ans = result
        return

    # 가지치기
    if result > ans:
        return

    # 열을 살펴보기
    for c in range(N):
        # 방문하지 않은 열이면
        if not visited[c]:
            visited[c] = 1 # 방문 표시
            min_v(r+1, result + V_arr[r][c]) # 다음 행에서 살펴보기
            visited[c] = 0 # 행을 전부 다 살펴봤으면 열 방문 초기화

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V_arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N # 열 방문 표시
    ans = 987654321

    min_v(0, 0)

    print('#{} {}'.format(tc, ans))

#################################################################
# 2. 비트 마스킹

# def factory(idx, s, visit):
#     global ans
#
#     # 모든 공장에 제품을 결정했다
#     if idx == N:
#         if s < ans:
#             ans = s
#     # 가지치기
#     elif s >= ans:
#         return
#
#     else:
#         for i in range(N): # 공장을 고르자
#             if visit & (1 << j):
#                 continue
#             factory(idx+1, s + cost[idx][j], visit | 1 << j)
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     cost = [list(map(int, input().split())) for _ in range(N)]
#
#     ans 987654321
#
#     factory(0, 0, 0)
#
#     print('#{} {}'.format(tc, ans))



