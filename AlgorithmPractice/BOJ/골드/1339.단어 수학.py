import sys
input = sys.stdin.readline

# 접근 방법: 자리수가 큰 알파벳 순으로 높은 수를 배정한다.

Numbers_dic = {
    'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0,
    'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0,
    'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0
}

N = int(input())
alpha_num_list = [input().strip() for _ in range(N)]

for alphabet in alpha_num_list:
    for j in range(len(alphabet)):
        num = 10 ** (len(alphabet) - j -1) # 자리수에 해당하는 알파벳에 10의 배수를 배정해준다.
        Numbers_dic[alphabet[j]] += num

nums = []
for value in Numbers_dic.values():
    if value > 0:
        nums.append(value)

nums.sort(reverse=True) # 내림차순으로 정렬하여 9부터 배정
ans = 0
for i in range(len(nums)):
    ans += nums[i] * (9 - i)
print(ans)


