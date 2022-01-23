import sys
input = sys.stdin.readline

# 접근방법: 각 등수에서 1등은 무조건 뽑히게 되어있다. 즉, 이 사람보다 다른 부분의 등수가 낮으면 탈락
T = int(input())
for tc in range(1, T+1):
    N = int(input())

    candidate = []
    for _ in range(N):
        s1, s2 = map(int, input().split())
        candidate.append((s1, s2))

    candidate.sort() # 서류점수를 기준으로 오름차순정렬
    max_pick = candidate[0][1]

    ans = 1 # 서류점수 1등은 이미 뽑았다.
    # 면접 점수로 비교
    for i in range(1, N):
        if max_pick > candidate[i][1]:
            ans += 1
            max_pick = candidate[i][1]

    print(ans)
