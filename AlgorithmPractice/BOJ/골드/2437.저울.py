import sys
from itertools import combinations
input = sys.stdin.readline


N = int(input().strip())
weights = list(map(int, input().split()))
weights.sort()

###################################
# 풀이 1: 조합 활용
# tmp = []
# for i in range(1, N+1):
#     tmp.append(list((combinations(weights, i)))) # 가능한 모든 조합 출력
#
# total_sum = []
# for i in tmp:
#     for j in i:
#         total_sum.append(sum(j)) # 계산 가능한 모든 무게 리스트
#
# total_sum.sort()
# total_sum = list(set(total_sum)) # 중복된 값 빼주기
#
# result = [0] * (sum(weights)+1) # 추를 통해 계산할 수 있는 무게 범위를 찾기
# for i in range(sum(weights)+1):
#     result[i] = i
# result.pop(0) # 무게 0은 빼주기
#
# # 측정 가능한 무게 찾기
# for num in total_sum:
#     if num in result:
#         result.remove(num)
#
# print(min(result))

#############################
# 풀이 2: 최적화(추가 담긴 리스트를 오름차순으로 정리해주고, 하나씩 더하면서 다음 요소와 비교한 후, 다음 추가 여태 더했던 추들의 합보다 더 크면 해당 값은 주어진 N개의 추들로 만들 수 없다.)
target = 1
for i in weights:
    if target < i:
        break
    target += i

print(target)






