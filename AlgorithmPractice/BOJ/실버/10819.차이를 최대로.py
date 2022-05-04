import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

per = permutations(numbers)
ans = -987654321

for i in per:
    tmp = 0
    for j in range(len(i) -1):
        tmp += abs(i[j] - i[j+1])
    # 최대값 구하기
    if tmp > ans:
        ans = tmp

print(ans)
