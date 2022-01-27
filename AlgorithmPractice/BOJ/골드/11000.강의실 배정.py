import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())
time_table = []

for _ in range(N):
    S, T = map(int, input().split())
    time_table.append((S, T))
time_table.sort()

queue = []
heapq.heappush(queue, time_table[0][1])

for i in range(1, N):
    if queue[0] > time_table[i][0]: # 현재 강의가 끝나는 시간보다 다음 강의 시작시간이 빠르면
        heapq.heappush(queue, time_table[i][1]) # 새로운 강의실 개설
    else: # 현재 강의실에서 이어서 강의 개최 가능
        heapq.heappop(queue) # 새로운 강의로 시간을 변경하기 위해 pop후 새로운 강의 시간 push
        heapq.heappush(queue, time_table[i][1])

print(len(queue))