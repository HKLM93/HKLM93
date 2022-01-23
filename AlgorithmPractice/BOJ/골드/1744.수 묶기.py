import sys
input = sys.stdin.readline

# 접근방법:
# 양수, 양수 = 곱셈 / 음수, 음수 = 곱셈 / 양수, 음수 = 덧셈 /
# 0, 양수 = 덧셈 / 0, 음수 = 곱셈 / 1, 양수 = 덧셈 / 1, 음수 = 덧셈

N = int(input())

positive_num = [] # 양수를 담을 리스트
negative_num = [] # 음수를 담을 리스트
one_num = [] # 1을 담을 리스트

for _ in range(N):
    num = int(input())

    if num > 1:
        positive_num.append(num)
    elif num <= 0:
        negative_num.append(num)
    else:
        one_num.append(num)

positive_num.sort(reverse=True) # 내림차순 정렬
negative_num.sort() # 오름차순 정렬

ans = 0
# 배열의 길이가 짝수이면 2개씩 곱해서 더해주기
if len(positive_num) % 2 == 0:
    for i in range(0, len(positive_num), 2):
        ans += positive_num[i] * positive_num[i+1]
# 배열의 길이가 홀수이면 마지막 요소는 놔두고 2개씩 곱해서 더해주기
else:
    for i in range(0, len(positive_num)-1, 2):
        ans += positive_num[i] * positive_num[i+1]
    # 마지막 숫자 더해주기
    ans += positive_num[-1]
# 배열의 길이가 짝수이면 2개씩 곱해서 더해주기
if len(negative_num) % 2 == 0:
    for i in range(0, len(negative_num), 2):
        ans += negative_num[i] * negative_num[i+1]
# 배열의 길이가 홀수이면 마지막 요소는 놔두고 2개씩 곱해서 더해주기
else:
    for i in range(0, len(negative_num)-1, 2):
        ans += negative_num[i] * negative_num[i+1]
    # 마지막 숫자 더해주기
    ans += negative_num[-1]

ans += sum(one_num)

print(ans)