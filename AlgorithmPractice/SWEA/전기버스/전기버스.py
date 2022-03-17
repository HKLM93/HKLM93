T = int(input())

for tc in range(1, T+1):
    # K: 버스가 한 번에 이동할 수 있는 거리
    # N: 마지막 종점의 위치(0번 정류장부터 출발)
    # M: 충전소의 개수
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split()))

    bus_stop = [0] * (N+1) # N번정류장까지 가야해서 +1을 해준다

    # 충전소 표시(charger를 순회)
    for i in charger:
        bus_stop[i] = 1

    # 또는 충전소 개수 순회
    # for i in range(M):
    #   bus_stop[charger[i]] = 1

    bus_idx = 0 # 버스의 위치
    ans = 0

    while True:
        # 버스가 이동할 수 있는 만큼 무조건 가
        bus_idx += K
        if bus_idx >= N: # N은 종점에 도착하거나 종점을 지나는 경우이기 때문
            break

        for i in range(bus_idx, bus_idx-K, -1):
            # 충전소에 있다면 버스 위치 갱신
            if bus_stop[i]:
                ans += 1
                bus_idx = i
                break

        # 충전소가 없는 경우 답이 존재하지 않는다.
        else:
            ans = 0
            break

    print('#{} {}'.format(tc, ans))



