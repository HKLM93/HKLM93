import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N: 끊어진 기타줄의 개수, M: 기타줄 브랜드의 개수

ans = 0
market = []

for _ in range(M):
    package_price, one_price = map(int, input().split())
    market.append([package_price, one_price])

package_list = sorted(market, key=lambda x: x[0])
one_list = sorted(market, key=lambda x: x[1])

# 패키지의 가격이 낱개 * 6의 가격보다 쌀 때
if package_list[0][0] <= one_list[0][1] * 6:
    ans = package_list[0][0] * (N//6) + one_list[0][1] * (N % 6)
    # 패키지 가격이 낱개 * (끊어진 기타줄의 수 + 1)보다 쌀 때
    if package_list[0][0] < one_list[0][1] * (N % 6):
        ans = package_list[0][0] * (N//6 + 1)

# 낱개 * 6의 가격이 패키지 가격보다 쌀 때
else:
    ans = one_list[0][1] * N

print(ans)
