import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(idx):
    global cnt
    visited[idx] = 1
    team.append(idx)

    if students[idx] == idx:
        team.pop()

    if visited[students[idx]] == 0:
        dfs(students[idx])
    else:
        if team:
            tmp = 0
            for j in range(len(team)):
                if team[j] != students[idx]:
                    tmp += 1
                else:
                    cnt += tmp
                    return
        cnt += len(team)
        return

T = int(input())
for tc in range(T):
    N = int(input())
    students = [0] + list(map(int, input().split()))

    visited = [0] * (N+1)
    cnt = 0
    for i in range(1, N+1):
       team = []
       if visited[i] == 0:
           dfs(i)

    print(cnt)

