import sys
input = sys.stdin.readline

# 접근 방법: '-'(빼기)를 기준으로 계산하면 된다. 즉, '+'(더하기)만 묶는다.

formula = list(input().strip().split('-'))
new_formula = []
for i in formula:
    result = 0
    s = i.split('+')
    for j in s:
        result += int(j)
    new_formula.append(result)

start = new_formula[0]
for i in range(1, len(new_formula)):
    start -= new_formula[i]

print(start)

