import sys
input = sys.stdin.readline

n = int(input())
student = []
for _ in range(n):
    name, birth_d, birth_m, birth_y = input().split()
    student.append([name, int(birth_d), int(birth_m), int(birth_y)])

student.sort(key=lambda x:(x[3], x[2], x[1]))
print(student[-1][0])
print(student[0][0])

# 나이가 가장 많은 사람 = 년, 월, 일이 가장 작은 사람
# 나이가 가장 적은 사람 = 년, 월, 일이 가장 큰 사람