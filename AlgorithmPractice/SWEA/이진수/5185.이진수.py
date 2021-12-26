import sys
sys.stdin = open('sample_input.txt', 'r')

# 16진수 딕셔너리
Hexadecimal = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

# 2진수 만들기
def make_binary(num):
    global result
    share, remainder = 0, 0
    # 4자리를 유지해야 하기 때문에 4번 반복
    for i in range(4):
        share = num // 2
        remainder = num % 2
        result = str(remainder) + result
        num = share
    return


T = int(input())
for tc in range(1, T+1):
    N, data = input().split()
    ans = ''

    for i in data:
        result = ''
        make_binary(Hexadecimal[i])
        ans += result

    print('#{} {}'.format(tc, ans))





