import sys
input= sys.stdin.readline

# dp 활용
N = int(input())
T_list = []
P_list = []
ans = [0] * (N+1)
for _ in range(N):
    t, p = map(int, input().split())
    T_list.append(t)
    P_list.append(p)

# 뒤에서부터 확인
for i in range(N-1, -1, -1):
    # 상담가능 기간이 퇴사날을 넘는 경우
    if T_list[i] + i > N:
        ans[i] = ans[i+1]
    else:
        ans[i] = max(P_list[i] + ans[i + T_list[i]], ans[i+1])

print(ans[0])


