import sys
input = sys.stdin.readline

N, M = map(int,input().split())
DNA = []
for _ in range(N):
    DNA.append(list(input().strip()))

cnt = 0
result = ''
for i in range(M):
    a, c, g, t = 0, 0, 0, 0
    for j in range(N):
        if DNA[j][i] == 'T':
            t+= 1
        elif DNA[j][i] == 'A':
            a += 1
        elif DNA[j][i] == 'G':
            g += 1
        elif DNA[j][i] == 'C':
            c += 1
    # 값이 같을 경우 사전순으로 출력해야함
    if max(a, c, g, t) == a:
        result += 'A'
        cnt += c + g + t
    elif max(a, c, g, t) == c:
        result += 'C'
        cnt += a + g + t
    elif max(a, c, g, t) == g:
        result += 'G'
        cnt += a + c + t
    elif max(a, c, g, t) == t:
        result += 'T'
        cnt += c + g + a

print(result)
print(cnt)

