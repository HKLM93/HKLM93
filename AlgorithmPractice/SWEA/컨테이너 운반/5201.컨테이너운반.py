import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight = sorted(list(map(int, input().split())), reverse=True)
    truck_weight = sorted(list(map(int, input().split())), reverse=True)

    ans = 0

    for i in range(N):
        for j in range(len(truck_weight)):
            if weight[i] <= truck_weight[j]:
                ans += weight[i]
                # 트럭에 화물을 실었으면 지우기
                truck_weight.pop(0)
                break
            else:
                break

    print('#{} {}'.format(tc, ans))


