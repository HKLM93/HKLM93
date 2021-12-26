import sys
sys.stdin = open('input.txt', 'r')

# 접근 방법
# 화폐 가치가 큰 것부터 순회하면서 화폐보다 크면 값에서 화폐 가치를 빼면서(또는 나눗셈을 활용) 카운트 한다.
def remain(num):

    if num >= 50000:
        money[0] = num // 50000
        num = num % 50000
    if num >= 10000:
        money[1] = num // 10000
        num = num % 10000
    if num >= 5000:
        money[2] = num // 5000
        num = num % 5000
    if num >= 1000:
        money[3] = num // 1000
        num = num % 1000
    if num >= 500:
        money[4] = num // 500
        num = num % 500
    if num >= 100:
        money[5] = num // 100
        num = num % 100
    if num >= 50:
        money[6] = num // 50
        num = num % 50
    if num >= 10:
        money[7] = num // 10


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    money = [0] * 8 # 각 인덱스는 앞에서부터 50000, 10000, 5000, 1000, 500, 100, 50, 10을 의미

    remain(N)

    ans = ' '.join(list(map(str, money)))

    print('#{}'.format(tc))
    print('{}'.format(ans))
