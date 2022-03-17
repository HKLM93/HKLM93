import sys
input = sys.stdin.readline

def find_ans(arr):
    arr.sort()
    arr[0], arr[1] = arr[0] + arr[1], arr[0] + arr[1]


n, m = map(int, input().split())
cards = list(map(int, input().split()))

for _ in range(m):
    find_ans(cards)

print(sum(cards))

