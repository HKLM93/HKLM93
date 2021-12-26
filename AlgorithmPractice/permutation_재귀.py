N = 3
arr = [1,2,3]

sel = [0] * N # 내가 직접 뽑은 것을 넣을 리스트
check = [0] * N # 내가 사용한 것을 체크할 리스트
def perm(idx):
    if idx == N:
        print(sel)
    else:
        for i in range(N):
            if check[i] == 0:
                sel[idx] = arr[i]
                check[i] = 1 # 사용했음을 체크
                perm(idx +1)
                check[i] =0 # 원상복귀

perm(0)
