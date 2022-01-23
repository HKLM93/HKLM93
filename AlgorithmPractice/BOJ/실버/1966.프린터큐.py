import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N은 문서의 개수, M: 몇번째로 인쇄되었는지 궁금한 문서의 위치
    importance = list(map(int, input().split()))

    idx = [0] * N

    idx[M] = 1

    cnt = 0
    while True:
        if importance[0] == max(importance):
            cnt += 1

            if idx[0] == 1:
                print(cnt)
                break
            else:
                importance.pop(0)
                idx.pop(0)
        else:
            importance.append(importance.pop(0))
            idx.append(idx.pop(0))
