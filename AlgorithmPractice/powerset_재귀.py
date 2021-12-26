N = 3
arr = [1,2,3]

# 비트 활용
for i in range(1 << N):
    for j in range(N):
        if i & 1 << j:
            print(arr[j], end='')
        print()

# powerset 재귀

sel = [0] * N

def powerset(idx):
    if idx == N:
        print(sel)
    else:
        # 뽑고가고
        sel[idx] = 1
        powerset(idx+1)
        # 안 뽑고가고
        sel[idx] = 0
        powerset(idx +1)

powerset(0)
