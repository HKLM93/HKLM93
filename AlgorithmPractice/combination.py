N = 4
R = 2

arr = [1, 2, 3, 4]
sel = [0] * R

# 조합
def comb(idx, s_idx): # idx는 arr을 도는 인덱스, s_idx는 sel을 도는 인덱스
    if s_idx == R:
        print(sel)
    elif idx == N:
        return
    else: 
        sel[s_idx] = arr[idx]
        comb(idx+1, s_idx +1) # 해당 idx번째 자리를 뽑거나
        comb(idx+1, s_idx) # 해당 idx번째 자리를 뽑지 않거나
comb(0, 0)

# 또 다른 방법
def combination(idx, s_idx): # idx: arr에서 시작하는위치
    if s_idx == R:  # s_idx: 내가 뽑고 있는 위치
        print(sel)
        return
    for i in range(idx, N):
        sel[s_idx] = arr[i]
        combination(i+1, s_idx+1)

combination(0,0)

# 적은 수를 뽑는 조합은 반복문으로도 가능하다
N = 4
#R = 3

array = [1, 2, 3, 4]
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            print(array[i], array[j], array[k])