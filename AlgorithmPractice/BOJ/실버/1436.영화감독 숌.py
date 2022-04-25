import sys
input = sys.stdin.readline

N = int(input())

cnt = 0
six_num = 666

while True:
    if '666' in str(six_num):
        cnt += 1
    if cnt == N:
        print(six_num)
        break
    six_num += 1