import sys
sys.stdin = open('s_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # Ai와 Bi 구하기
    road = [0] * 5001 # Ai와 Bi의 범위가 5000까지라서
    # 버스가 지나는 정류장 카운트
    for i in range(N):
        Ai, Bi = map(int, input().split())
        for j in range(Ai, Bi+1):
            road[j] += 1

    P = int(input())

    print('#{}'.format(tc), end = ' ')
    for s in range(P):
        Cj = int(input()) # 정류장 번호
        print(road[Cj], end = ' ')
    print()












