import sys
input = sys.stdin.readline

N, L = map(int, input().split()) # N: 물이 새는 곳의 개수, L: 테이프의 길이
leak = list(map(int, input().split())) # 물이 새는 곳의 위치
leak.sort()

start = leak[0] # 시작점
end = leak[0] + L # 끝나는 지점(테이프 길이를 더한 값)
cnt = 1 # 테이프의 개수

for i in range(N):
    # 물이 새는 곳이 시작점과 끝나는 지점 사이에 있을 때
    if start <= leak[i] < end:
        continue
    # 아니라면 시작점과 끝점 갱신
    else:
        start = leak[i]
        end = leak[i] + L
        cnt += 1
print(cnt)


