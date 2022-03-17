import sys
input = sys.stdin.readline

word = input().strip()

word = word + '00' # 인덱스 오류 방지를 위해 의미 없는 문자 2개를 넣어줌
N = len(word)
cnt = 0
i = 0
while i < N-2:
    if (word[i] == 'c' and word[i+1] == '=') or (word[i] == 'c' and word[i+1] == '-') or (word[i] == 's' and word[i+1] == '=') or (word[i] == 'z' and word[i+1] == '=') or (word[i] == 'd' and word[i+1] == '-') or (word[i] == 'l' and word[i+1] == 'j') or (word[i] == 'n' and word[i+1] == 'j'):
        cnt += 1
        i += 2
    elif word[i] =='d' and word[i+1] == 'z' and word[i+2] =='=':
        cnt += 1
        i += 3
    else:
        cnt += 1
        i += 1

print(cnt)
