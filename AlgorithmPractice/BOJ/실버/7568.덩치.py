import sys
input = sys.stdin.readline

N = int(input())
students = []
for _ in range(N):
    w, h = map(int, input().split())
    students.append((w, h))

for i in range(len(students)):
    rank = 1
    for j in range(len(students)):
        if students[i][0] < students[j][0] and students[i][1] < students[j][1]:
            rank += 1
    print(rank, end=' ')

