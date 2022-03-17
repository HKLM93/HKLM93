import sys
input = sys.stdin.readline


def path_check(path):
    sw = [False] * N

    for i in range(N-1):
        # 높이가 같을 때
        if path[i] == path[i+1]:
            continue
        # 경사가 2이상일 때
        if abs(path[i] - path[i+1]) > 1:
            return False
        # 경사가 1이고 내리막길일 때
        if path[i] > path[i+1]:
            tmp = path[i+1]
            # 경사로 체크
            for j in range(i+1, i+1+L):
                if 0 <= j < N:
                    # 경사로를 놓아야 하는데 높이가 다를 때
                    if path[j] != tmp:
                        return False
                    if sw[j] == True:
                        return False
                    sw[j] = True
                else:
                    return False
        # 경사가 1이고 오르막길일 때
        else:
            tmp = path[i]
            # 경사로 체크
            for j in range(i, i-L, -1):
                if 0 <= j < N:
                    # 경사로를 놓아야 하는데 높이가 다를 때
                    if path[j] != tmp:
                        return False
                    if sw[j] == True:
                        return False
                    sw[j] = True
                else:
                    return False
    # 모든 조건을 통과하면 경로가 가능
    return True

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0 # 경로의 개수

# 행 확인
for r in arr:
    if path_check(r):
        cnt += 1
# 열 확인
for i in range(N):
    tmp = []
    for j in range(N):
        tmp.append(arr[j][i])
    if path_check(tmp):
        cnt += 1
print(cnt)

