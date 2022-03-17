import sys
sys.stdin = open('s_input.txt', 'r')

def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])

def union(x, y):
    parent[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N: 창용마을에 사는 사람의 수(정점의 개수), M: 알고 있는 사람의 관계의 수(간선의 개수)

    # 대표자 리스트
    parent = [0] * (N+1)
    for i in range(1, N+1):
        parent[i] = i

    #  아는 사람끼리 연결하고 대표자 뽑기
    for _ in range(M):
        s, e = map(int, input().split())
        union(s, e)

    # 최종적으로 모두 연결하기
    result = []
    for i in range(N+1):
        result.append(find_set(i))

    ans = len(set(result)) - 1 # 0번 인덱스는 편의를 위해 넣었기 때문에 빼주어야 한다.

    print('#{} {}'.format(tc, ans))

##########################################
# rank 활용
# def make_set(x):
#     p[x] = x
#     rank[x] = 0
# def find_set(x):
#   if p[x] != x:
#       p[x] = find_set(p[x])
#    return p[x]
# def union(x, y):
#     px = find_set(x)
#     py = find_set(y)
#
#     if rank[px] > rank[py]:
#         p[py] = px
#     else:
#         p[px] = py
#
#         if rank[px] == rank[py]:
#             rank[py] += 1

# parent = [0] * (N+1)
# rank = [0] (N+1)
# for i in range(N+1):
#     make_set(i)
