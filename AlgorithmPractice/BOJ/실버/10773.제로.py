import sys
input = sys.stdin.readline

K = int(input().strip())

Numbers = []

for _ in range(K):
    num = int(input().strip())
    if num != 0:
        Numbers.append(num)
    else:
        Numbers.pop(-1)

print(sum(Numbers))


