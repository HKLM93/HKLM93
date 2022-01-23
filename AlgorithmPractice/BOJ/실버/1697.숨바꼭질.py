import sys

# 접근 방법: N에서 -1, +1, x2의 경우가 다음 노드이다. 이어진 노드를 BFS로 탐색하여 K를 찾으면 된다.

def BFS(S): # S는 시작점
    queue = [S]
    distance = [0] * 100001 # 거리 계산을 위함

    while queue:
        v = queue.pop(0) # v는 노드

        if v == K: # 도착지점에 도착하면 반복문 종료
            print(distance[v]) # 거리를 출력
            break
        for i in (v-1, v+1, v*2): # '노드-1', '노드+1', '노드*2' 순회
            if 0 <= i <= 100000 and not distance[i]:
                queue.append(i)
                distance[i] = distance[v] + 1


N, K = map(int, input().split()) # N은 수빈이의 위치, K는 동생의 위치

BFS(N)

