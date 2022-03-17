import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = list(map(int, input().split()))
    # 시작 페이지(l)는 1, 끝 페이지(r)는 P
    l = 1
    r = P
    # 책의 페이지를 순회해야 하니 리스트로 나타냄
    book = list(range(r+1))

    # A의 이진 검색
    cnt_1 = 0
    while l <= r:
        cnt_1 += 1
        c = int((l+r)//2)
        # 검색 성공
        if book[c] == Pa:
            break
        # 검색해서 없을 경우 범위를 줄임
        elif book[c] > Pa:
            r = c - 1
        else:
            l = c + 1

    # B의 이진검색
    # 시작 페이지(l)는 1, 끝 페이지(r)는 P로 초기화 해준다
    l = 1
    r = P
    cnt_2 = 0

    while l <= r:
        cnt_2 += 1
        c = int((l + r) // 2)
        # 검색 성공
        if book[c] == Pb:
            break
        # 검색해서 없을 경우 범위를 줄임
        elif book[c] > Pb:
            r = c
        else:
            l = c

    # A와 B 중 승자 출력
    if cnt_1 < cnt_2:
        print('#{} {}'.format(tc, 'A'))
    elif cnt_1 > cnt_2:
        print('#{} {}'.format(tc, 'B'))
    else:
        print('#{} {}'.format(tc, '0'))







