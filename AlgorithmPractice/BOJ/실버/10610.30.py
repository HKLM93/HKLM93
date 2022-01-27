import sys
input = sys.stdin.readline

# 30이 배수가 되는 조건: 10으로 나누어서 3의 배수가 되면 됨

## 내 답안
# def check_30(num):
#     tmp = num % 10
#     # 10으로 나누어서 정수일 때
#     if tmp == 0:
#         total = 0
#         while tmp > 10:
#             total += tmp % 10
#             tmp = tmp // 10
#         total += tmp
#
#         # 모든 자릿수를 더한 숫자가 3의 배수이면 찾는 숫자
#         if total % 3 == 0:
#             return num
#         # 아니면 찾는 숫자가 없음
#         else:
#             return -1
#     # 아니면 찾는 숫자가 없음
#     else:
#         return -1

#####################################

N = list(input().strip())
N.sort(reverse=True)
total = 0

## 모범답안
for i in N:
    total += int(i)

if total % 3 != 0 or '0' not in N:
    print(-1)
else:
    print(''.join(N))




