import sys
input = sys.stdin.readline

word = list(input())
word.pop(-1)
word.sort(reverse=True)
ans = ''.join(word)

print(ans)