import sys
input = sys.stdin.readline

word = input().strip()
target = input().strip()

idx = 0 # 인덱스
cnt = 0 # 찾은 단어의 개수

while idx <= len(word) - len(target): # idx는 전체 단어 개수 - 찾아야할 단어의 개수
    if word[idx:idx+len(target)] == target: # 찾아야 할 단어의 길이만큼 비교
        # 찾았으니 카운트
        cnt += 1
        # 찾아야 할 단어의 길이만큰 인덱스 옮기기
        idx += len(target)
    # 못찾았으면
    else:
        # 인덱스는 하나만 증가
        idx += 1

print(cnt)

