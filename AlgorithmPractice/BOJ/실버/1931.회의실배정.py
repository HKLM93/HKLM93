import sys
input = sys.stdin.readline

# 접근 방법: 회의의 시작 시간을 첫번째, 끝나는 시간을 두번째로 기준으로 해 정렬 후 이전 시작 시간보다 다음 끝나는 시간이 큰 경우를 선택한다.

N = int(input()) # N: 회의의 수

time = [[0] * 2 for _ in range(N)]
for i in range(N):
    s, e = map(int, input().split())
    time[i][0] = s
    time[i][1] = e

time.sort(key = lambda x: (x[1], x[0]))

cnt = 1 # 회의의 개수
end_time = time[0][1]
for i in range(1, N):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]

print(cnt)