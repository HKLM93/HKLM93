import sys
input = sys.stdin.readline

N = int(input())
people = list(map(int, input().split()))
watcher = list(map(int, input().split())) # 총감독관의 감시 수, 부감독관의 감시 수

B = watcher[0]
C = watcher[1]

cnt = 0
for i in range(len(people)):
    people[i] = people[i] - B
    cnt += 1 # 총감독관은 한 시험장에 1명씩 있어야 한다.

    if people[i] <= 0: # 0보다 작거나 같으면 총감독관이 시험장을 모두 감독할 수 있음
        pass
    else: # 부감독관이 필요함
       tmp = people[i] // C
       cnt += tmp # 부감독관은 시험자 수를 나눈 값
       if people[i] % C != 0: # 인원이 남으면 부감독관 1명 추가
           cnt += 1

print(cnt)
