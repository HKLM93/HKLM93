import sys
sys.stdin = open('sample_input.txt', 'r')

# 나올 수 있는 숫자들을 찾음
def check_num(num1, num2):

    dec_two = int(num1, 2)
    dec_three = int(num2, 3)

    # 2진법에서 나올 수 있는 수들
    for n, val in enumerate(list(map(int, num1))[::-1]):
        for j in range(2):
            if val == j:
                continue
            tmp1 = dec_two - val * (2**n) + j * (2 ** n)

            if tmp1 not in binary:
                binary.append(tmp1)
            else:
                return tmp1

    # 3진법에서 나올 수 있는 수들
    for n, val in enumerate(list(map(int, num2))[::-1]):
        for j in range(3):
            if val == j:
                continue
            tmp2 = dec_three - val * (3 ** n) + j * (3 ** n)

            if tmp2 not in ternary:
                ternary.append(tmp2)
            else:
                return tmp2

T = int(input())
for tc in range(1, T+1):
    bin_num = input()
    tern_num = input()

    binary = []
    ternary = []

    check_num(bin_num, tern_num)

    ans = 0

    # 공통된 숫자가 있으면 답
    for i in binary:
        for j in ternary:
            if i == j:
                ans = i

    print('#{} {}'.format(tc, ans))

##############################################33
# 10진법 만들기 함수 = int(0진법수, 0진법)
# def change_to_dec(num, notation):
#     tmp = 0
#
#     for n, val in enumerate(list(map(int, num))[::-1]):
#         tmp += val*(notation**n)
#     return tmp
#
# def change_to_dec2(num, notation):
#     tmp = 0
#     n = len(num) - 1
#
#     for i in map(int, num):
#         tmp += i * (notation ** n)
#         n -= 1
#
#     return tmp

#################################################
# 두번째 풀이
# def check2():
#     bi_num = 0
#
#     for x in bi:
#         bi_num = bi_num * 2 + int(x)
#
#     for i in range(len(bi)):
#         binary.append(bi_num ^ (1 << i))
#
#     for i in range(len(tr)):
#         num1 = 0
#         num2 = 0
#         for j in range(len(tr)):
#             if i != j:
#                 num1 = num1 * 3 + int(tr[j])
#                 num2 = num2 * 3 + int(tr[j])
#             else:
#                 num1 = num1 * 3 + int(tr[j] + 1) % 3
#                 num2 = num2 * 3 + int(tr[j] + 2) % 3
#
#         if num1 in binary:
#             return num1
#         if num2 in binary:
#             return num2
#
# T = int(input())
#
# for tc in range(1, T+1):
#     bi = input()
#     tr = input()
#
#     binary = []
#
#     check2()