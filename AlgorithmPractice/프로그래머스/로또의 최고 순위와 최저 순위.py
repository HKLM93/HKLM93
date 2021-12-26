# 프로그래머스 코딩 테스트 연습 level 1

def solution(lottos, win_nums):
    cnt = 0 # 당첨된 숫자를 세기 위함
    tmp = 0 # 가려진 숫자를 세기 위함
    answer = [0, 0]

    for i in range(len(lottos)):
        if lottos[i] == 0:
            tmp += 1
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                cnt += 1
    # 당첨된 숫자의 개수에 따른 최소 등수
    if cnt == 2:
        answer[1] = 5
    elif cnt == 3:
        answer[1] = 4
    elif cnt == 4:
        answer[1] = 3
    elif cnt == 5:
        answer[1] = 2
    elif cnt == 6:
        answer[1] = 1
    else:
        answer[1] = 6

    # 가려진 숫자에 따른 최대 등수
    count = tmp + cnt

    if count == 2:
        answer[0] = 5
    elif count == 3:
        answer[0] = 4
    elif count == 4:
        answer[0] = 3
    elif count == 5:
        answer[0] = 2
    elif count == 6:
        answer[0] = 1
    else:
        answer[0] = 6

    return answer