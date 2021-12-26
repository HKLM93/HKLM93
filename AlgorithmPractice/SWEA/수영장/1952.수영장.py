import sys
sys.stdin = open('sample_input.txt', 'r')

# 최소비용 찾기(모든 경우의 수를 탐색)
def find_min(m, cost):
    global min_cost
    # 13월은 없어서 12월이 넘어가면 최소비용 계산
    if m > 12:
        if min_cost > cost:
            min_cost = cost
        return

    # m월에 1일권 구입
    find_min(m+1, cost + d*month[m])
    # m월에 1달권 구입
    find_min(m+1, cost + m1)
    # m월에 3달권 구입
    find_min(m+3, cost + m3)

T = int(input())
for tc in range(1, T+1):
    d, m1, m3, y = map(int, input().split()) # 일일권, 한달권, 세달권, 일년권 가격
    month = [0] + list(map(int, input().split())) # 계산의 편의를 위해 0번 인덱스에 0을 넣어줌

    # 1년간 최소 비용은 일년권의 가격이고 수영장 이용기간이 1년보다 적을 경우 최소비용은 일년권의 가격보다 낮아질 것이다.
    min_cost = y

    find_min(1, 0) # 1월부터 이용금액 0원으로 계산 시작

    print('#{} {}'.format(tc, min_cost))


##############################################
# 교수님 답안(DP: 동적 프로그래밍) - 참고용
#
#
# T = int(input())
# for tc in range(1, T+1):
#     d, m1, m3, y = map(int, input().split()) # 일일권, 한달권, 3달권, 연권
#     month = [0] + list(map(int, input().split()))
#
#     dp = [0] * 13
#
#     dp[1] = min(m1, month[1] * d)
#     dp[2] = dp[1] + min(m1, month[2] * d)
#
#     for i in range(3, 13):
#         dp[i] = min(dp[i-3] + m3, dp[i-1] + m1. dp[i-1] + month[i] * d )
#
#     print('#{} {}'.format(tc, min(dp[12, y])))