T = int(input())

for tc in range(1, T+1):
    N = int(input())
    box = list(map(int, input()))

    ans = 0

    # 전체 모든 박스 비교
    for i in range(N):
        cnt = 0

        # 나 다음부터 나보다 작은 값을 찾아 카운트
        for j in range(i+1, N):
            if box[i] > box[j]:
                cnt +=1

        if ans < cnt:
            ans = cnt
    print("#{} {}".format(tc, ans))
