import sys
input = sys.stdin.readline

N = int(input()) # N:센서의 개수
K = int(input()) # K: 최대로 세울 수 있는 집중국의 수

# 센서는 적어도 하나의 집중국과 통신이 가능해야 함
# 각 집중국의 수신 가능 영역 길이의 합이 최소가 되야 함

sensers = list(map(int, input().split()))
sensers.sort()

# K >= N 이면 센서 자리에 세우면 된다.
if K >= N:
    print(0)
else:
    # 아닐 때는 센서들을 K개의 구간으로 나누어야 한다.
    gap = []
    for i in range(1, N):
        gap.append(sensers[i] - sensers[i-1])
    gap.sort()
    
    # K-1번만큼 가장 큰 원소부터 제거 해야 한다.
    for _ in range(K-1):
        gap.pop(-1)

    print(sum(gap))
