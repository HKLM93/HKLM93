import sys
input = sys.stdin.readline

def min_money(num):

    cnt = 0 # 화폐의 개수

    for i in range(N):
        # 돈이 0이 되면 종료
        if num == 0:
            break
        # 현재 화폐가 돈보다 크면 넘어감
        if money[i] > num:
            continue
        # 화폐의 개수는 만들어야 하는 돈 / 화폐의 몫
        cnt += num // money[i]
        # 나누고 남은 돈이 다음 돈
        num = num % money[i]

    return cnt

N, K = map(int, input().split())

money = [0]*N

for i in range(N):
    money[i] = int(input())

money = money[::-1] # 내림차순 정렬

print(min_money(K))


