# 선형 큐
front = rear = -1
N = 100
Q = [0] * N

# 큐 삽입
def enqueue(item):
    global rear
    # is_full 검사
    if rear == N-1:
        print('가득 찼음')
    else:
        rear += 1
        Q[rear] = item
# 큐 삭제
def dequeue():
    global front
    # is_empty 필요
    if front == rear:
        print('비었다')
    else:
        front += 1
        return Q[front]

enqueue(1)
enqueue(2)
enqueue(3)

print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())

# 리스트 큐
Q = []

for i in range(10000): # 리스트의 인덱스가 10만개 이상부터 컴퓨터에 부담이 간다.
    print(Q.append(i)) 

for i in range(10000): # 앞에 있는 것을 뺐을 때 나머지들이 앞으로 밀착을 하기 때문에 부담이 가는 것
    print((Q.pop(0)))

# 원형큐
front = rear = 0
N = 10 # Q size이다.
Q = [0] * N

# 큐 삽입
def enqueue(item):
    global rear
    # is_full 검사
    if (rear+1) % N: == front:
        print('가득 찼음')
    else:
        rear = (rear +1) % N
        Q[rear] = item
# 큐 삭제
def dequeue():
    global front
    # is_empty 필요
    if front == rear:
        print('비었다')
    else:
        front = (front+1) % N
        return Q[front]

for i in range(100):
    enqueue(i)

for i in range(100):
    dequeue(i)

# deque
from collections import deque
dq = deque()
for i in range(10000):
    dq.append(i)
for i in range(10000):
    print(dq.popleft())