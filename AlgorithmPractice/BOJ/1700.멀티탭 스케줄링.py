import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # N: 멀티탭 구멍의 개수, K: 전기용품 총 사용 횟수
gadget = list(map(int, input().split()))
multitap = []
cnt = 0

for i in range(K):
    # 멀티탭에 이미 기계가 꽃혀있는 경우
    if gadget[i] in multitap:
        continue
    # 멀티탭에 빈 곳이 있는 경우
    if len(multitap) < N:
        multitap.append(gadget[i])
        continue
    # 멀티탭이 꽉 찬 경우
    idxs = [] # 다음 멀티탭의 값을 저장
    flag = True
    for j in range(N):
        # 남은 전기용품 사용 중에서 멀티탭에 꽃혀 있는 경우
        if multitap[j] in gadget[i:]:
            idx = gadget[i:].index(multitap[j])
        else:
            idx = 101
            flag = False

        idxs.append(idx)

        if flag == False:
            break
    out = idxs.index(max(idxs))
    del multitap[out] # del: 인덱스로 삭제하는 함수
    multitap.append(gadget[i])
    cnt += 1
print(cnt)

