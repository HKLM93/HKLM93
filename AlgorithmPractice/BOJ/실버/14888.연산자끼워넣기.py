import sys
input = sys.stdin.readline

def dfs(depth, total, plus, minus, multiply, divide):
    global max_ans, min_ans

    # 수를 다 계산했을 때
    if depth == N:
        max_ans = max(total, max_ans)
        min_ans = min(total, min_ans)
        return

    # 더하기가 존재할 때
    if plus:
        dfs(depth+1, total + Numbers[depth], plus-1, minus, multiply, divide)
    # 빼기가 존재할 때
    if minus:
        dfs(depth + 1, total - Numbers[depth], plus, minus-1, multiply, divide)
    # 곱하기가 존재할 때
    if multiply:
        dfs(depth + 1, total * Numbers[depth], plus, minus, multiply-1, divide)
    # 나누기가 존재할 때
    if divide:
        dfs(depth + 1, int(total / Numbers[depth]), plus, minus, multiply, divide-1)

N = int(input()) # 수의 개수
Numbers = list(map(int, input().split())) #수열(단, 주어진 수의 순서를 바꿔서는 안 된다)
Operation = list(map(int, input().split())) # +, -, * /의 개수

# -10억에서 10억까지 존재하기 때문에
max_ans = -1000000001
min_ans = 1000000001

dfs(1, Numbers[0], Operation[0], Operation[1], Operation[2], Operation[3])

print(max_ans)
print(min_ans)
