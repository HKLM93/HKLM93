import sys
input = sys.stdin.readline

word = input().strip()

reversed_word = ''

i = 0 # 문자열의 인덱스 초기화

while i < len(word):
    if word[i] == '<': # <를 만나면 >를 만날때까지 저장
        reversed_word += '<'
        i += 1
        while word[i] != '>':
            reversed_word += word[i]
            i += 1
        reversed_word += '>'
        i += 1
    elif word[i].isalnum(): # 숫자나 영어인 경우
        tmp = []  # 뒤집을 문자를 집어넣을 리스트
        while i < len(word) and word[i].isalnum():
            tmp.append(word[i])
            i += 1
        rev_tmp = ''.join(tmp[::-1]) # 슬라이싱을 통해서 문자를 뒤집음
        reversed_word += rev_tmp
    else:
        reversed_word += word[i] # 빈칸인 경우 빈 칸을 넣고 다음 인덱스로
        i += 1

print(reversed_word)


### 시간이 오래걸린다 ㅠㅠㅠ


