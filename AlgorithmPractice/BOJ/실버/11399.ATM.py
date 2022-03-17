import sys
input = sys.stdin.readline

def find_min(lst):
    global ans

    cnt = 0
    for i in person:
        cnt += i
        ans += cnt

N = int(input())
person = list(map(int, input().split()))
person.sort() # 오름차순으로 정렬하면 최소값이 나온다.
ans = 0

find_min(person)

print(ans)
