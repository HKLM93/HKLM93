import sys
sys.stdin = open('sample_input.txt', 'r')

# 내림차순 정렬
def sorting(arr):
    for i in range(N-1):
        if arr[i][1] < arr[i+1][1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            sorting(arr)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    schedule = []
    for _ in range(N):
        s, e = map(int, input().split())
        schedule.append([s, e])

    # 내림차순 정렬
    sorting(schedule)
    # 도킹 시간을 담을 리스트
    doking = []
    # 가장 빨리 끝나는 화물 가져오기
    start, end = schedule.pop()
    # 도킹에 담기
    doking.append([start, end])

    while schedule:
        next_start, next_end = schedule.pop()
        #  이전 화물 끝나는 시간보다 늦게 시작하면
        if end <= next_start:
            # 도킹 리스트에 담고
            doking.append([next_start, next_end])
            # 시작시간과 끝나는 시간을 갱신해줌
            start, end = next_start, next_end

    print('#{} {}'.format(tc, len(doking)))