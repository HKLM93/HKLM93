import sys
sys.stdin = open('sample_input.txt', 'r')

# 서로소를 구해서 대표자의 수를 구하면 된다.
def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])

def union(x, y):
    parent[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N은 사람 수, M은 신청서 수

    # 대표자 구하기
    parent = [0] * (N+1)
    for i in range(1, N+1):
        parent[i] = i

    combi = list(map(int, input().split()))
    for i in range(len(combi)//2):
        n1, n2 = combi[2*i], combi[2*i+1]
        # 짝꿍 만들기
        union(n1, n2)

    # 그룹 지어주기(대표자를 기준으로)
    result = []
    for i in range(len(parent)):
        result.append(find_set(i))

    ans = len(set(result)) -1 # 각 번호의 사람의 대표자를 뽑았으니 중복을 지워준다. 그리고 0번 인덱스는 사용하지 않는다

    print('#{} {}'.format(tc, ans))


#############################################################
# bfs 활용(그룹을 연결된 노드처럼 생각)

# def bfs(st):
#     Q = [st]
#     team[st] = 1
#
#     while Q:
#         p = Q.pop(0)
#
#         for i in range(1, N+1):
#             if not team[i] and adj_arr[p][i]:
#                 team[i] = 1
#                 Q.append(i)
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#
#     edges = list(map(int, input().split()))
#
#     adj_arr = [[0]*(N+1) for _ in range(N+1)] # 인접행렬
#
#     for i in range(0, len(edges), 2):
#         a = edges[i]
#         b = edges[i+1]
#
#         adj_arr[a][b] = adj_arr[b][a] = 1 # 방향성이 없다
#
#     ans = 0
#
#     team = [0] * (N+1)
#
#     for i in range(1, N+1):
#         if not team[i]:
#             ans += 1
#             bfs(i)
#
#     print(ans)