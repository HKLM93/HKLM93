import sys
input = sys.stdin.readline

N = int(input())
words = set()
for _ in range(N):
    words.add(input().strip())
words = list(words)
words.sort()
words.sort(key=len)

for i in words:
    print(i)