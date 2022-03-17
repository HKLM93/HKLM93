import sys
input = sys.stdin.readline

word = list(input().strip())
check = ['U', 'C', 'P', 'C']

cnt = 0
for i in check:
    if i in word:
        cnt += 1
        word = word[word.index(i)+1:]
    else:
        print('I hate UCPC')
        break
if cnt == 4:
    print('I love UCPC')


