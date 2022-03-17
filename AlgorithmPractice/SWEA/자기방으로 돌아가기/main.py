import sys
sys.stdin = open('sample_input.txt', 'r')

def div(num):
    return (int(num) + 1) // 2

def find_max(num):
    max_value = num[0]
    for i in range(1, len(num)):
        if max_value < num[i]:
            max_value = num[i]
    return max_value

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 돌아갈 사람의 수

    students = [list(map(div, input().split()))for _ in range(N)]

    corridor = [0] * 201

    for i in range(N):
        if students[i][0] > students[i][1]:
            students[i][0], students[i][1] = students[i][1], students[i][0]

        for j in range(students[i][0], students[i][1] +1):
            corridor[j] += 1

    print('#{} {}'.format(tc, find_max(corridor)))


