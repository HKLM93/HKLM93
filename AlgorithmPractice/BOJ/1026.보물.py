import sys
input = sys.stdin.readline

# 접근방법: A를 내림차순, B를 오름차순으로 정렬 후 각 인덱스에 해당하는 수를 곱하면 된다.

N = int(input())
array_A = list(map(int, input().split()))
array_B = list(map(int, input().split()))

sorted_A = sorted(array_A, reverse=True)
sorted_B = sorted(array_B)

ans = 0
for i in range(N):
    ans += (sorted_A[i] * sorted_B[i])

print(ans)
