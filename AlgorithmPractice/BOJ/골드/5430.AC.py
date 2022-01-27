
# 내 코드
import sys
from collections import deque
input = sys.stdin.readline


T = int(input())
for tc in range(T):
    P = input().strip() # 수행할 함수
    N = int(input()) # 배열에 들어있는 수의 개수
    arr = deque(input().strip()[1:-1].split(','))
    if N == 0:
        arr = deque()

    if P.count('D') > len(arr):
        print('error')
        continue

    for cmd in P:
        if cmd == 'R' and P.count('R') % 2:
            arr.reverse()
        elif cmd == 'D':
            arr.popleft()
    print("[" + ",".join(arr) + "]")

###############################################

# 나와 비슷한 코드의 모범 답안
import sys
from collections import deque
from collections import Counter

# 테스트케이스 입력 받은 만큼 반복
for _ in range(int(sys.stdin.readline())):
    try:						# 에러를 잡기 위한 try-except
        p = sys.stdin.readline()			# 명령어 입력
        n = int(sys.stdin.readline())			# 배열 원소 수
        arr = sys.stdin.readline()[1:-2]		# 배열 입력. 앞뒤의 [] 및 맨 마지막 \n 제거.
        if len(arr) > 0:				# arr이 비어있지 않다면
            arr = deque(map(int, arr.split(',')))	# , 로 구분하여 큐로 변환
        else:						# arr가 비었다면
            arr = deque(arr)				# 그 상태로 큐료 변환

        isAsc = True					# R 추적.

        # D의 개수를 n과 비교하여 n보다 많으면 에러 생성, 같으면 [] 출력 후 다음으로 넘김
        if 'D' in p:
            num_p = Counter(p).get('D')
            if num_p > n:
                raise ValueError
            elif num_p == n:
                print("[]")
                continue

        for cmd in p:					# 각 명령어마다 순서대로 실행
            if cmd == 'R':				# R이면 isAsc만 변경
                isAsc = not isAsc
            if cmd == 'D':				# D이면 isAsc의 값에 따라 pop 또는 popleft
                if isAsc:
                    arr.popleft()
                else:
                    arr.pop()
        else:						# for문이 끝난 후
            if not isAsc:				# isAsc가 false이면 arr 뒤집음
                arr.reverse()
            print(str(list(arr)).replace(' ', ''))	# arr을 문자열로 변환, 공백 제거 후 출력
    except:						# 에러 발견 시 'error' 출력
        print("error")

###############################################33
## 가장 시간이 짧은 코드
import sys
from collections import deque

t = int(input())

for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    queue = deque(arr)

    rev, front, back = 0, 0, len(queue)-1
    flag = 0
    if n == 0:
        queue = []
        front = 0
        back = 0

    for j in p:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")





