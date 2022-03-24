import sys
input = sys.stdin.readline

A, B = map(int, input().split())

arr = [0]
for i in range(46): # 범위가 1000까지라 46까지만 확인하면 된다.
    for j in range(i):
        arr.append(i)

print(sum(arr[A:B+1]))