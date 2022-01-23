import sys
input = sys.stdin.readline

T = int(input())
ans = 0 # 그룹 단어의 개수
for tc in range(1, T+1):
    word = input().strip()
    cnt = 0 # 그룹 단어가 아닌 단어의 개수

    for idx in range(0, len(word)-1):
        if word[idx] != word[idx+1]:
            new_word = word[idx+1:]
            # 새로운 단어에 이전 단어가 존재하면
            if new_word.count(word[idx]) > 0:
                # 그룹 단어가 아님
                cnt += 1
    if cnt == 0:
        ans += 1

print(ans)
