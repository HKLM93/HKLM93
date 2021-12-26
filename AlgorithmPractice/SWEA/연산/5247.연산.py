import sys
from collections import deque
sys.stdin = open('sample_input.txt', 'r')

# bfs
def calculate(N, cnt): # cnt는 연산횟수
    global ans

    queue = deque()
    queue.append((N, cnt))

    while queue:
        num, cnt = queue.popleft() # num은 중간 연산 결과

        # M을 찾으면 함수 종료
        if num == M:
            ans = cnt
            return

        # 4가지 경우 순회
        for i in range(4):
            # +1일 때
            if i == 0:
                next_num = num + 1
                # 가지치기(범위를 벗어나거나 한 번 나왔던 값이면 계산 안 하도록)
                if 0 < next_num <= 1000000 and visited[next_num] == 0:
                    queue.append((next_num, cnt+1))
                    visited[next_num] = 1 # 방문 체크
            # -1일때
            elif i == 1:
                next_num = num - 1
                # 가지치기(범위를 벗어나거나 한 번 나왔던 값이면 계산 안 하도록)
                if 0 < next_num <= 1000000 and visited[next_num] == 0:
                    queue.append((next_num, cnt+1))
                    visited[next_num] = 1 # 방문 체크
            # *2일 때
            elif i == 2:
                next_num = num * 2
                # 가지치기(범위를 벗어나거나 한 번 나왔던 값이면 계산 안 하도록)
                if 0 < next_num <= 1000000 and visited[next_num] == 0:
                    queue.append((next_num, cnt+1))
                    visited[next_num] = 1 # 방문 체크
            # -10일 때
            else:
                next_num = num - 10
                # 가지치기(범위를 벗어나거나 한 번 나왔던 값이면 계산 안 하도록)
                if 0 < next_num <= 1000000 and visited[next_num] == 0:
                    queue.append((next_num, cnt+1))
                    visited[next_num] = 1 # 방문 체크

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001 # 방문 확인, 백만이 최대라서

    ans = 0

    calculate(N, 0)

    print('#{} {}'.format(tc, ans))

################################################################################################
# bfs 활용(트리를 생각해보면 접근할 수 있다)
# from collections import deque
#
# def bfs():
#     Q = deque()
#     Q.append(N)
#     memo[N] = True
#
#     ans = 0
#
#     while Q:
#         size = len(Q)
#
#         for i in range(size):
#             num = Q.popleft()
#
#             if num == M: return ans
#
#             for j in (num+1, num-1, num*2, num-10):
#                 if 0 < j <= 1000000 and memo[j]:
#                     memo[j] = True
#                     Q.append(j)
#
#         ans += 1
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#
#     memo = [False] * 1000001
#
#     bfs()



