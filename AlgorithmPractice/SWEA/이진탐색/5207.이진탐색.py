import sys
sys.stdin = open('sample_input.txt', 'r')

def binary_search(arr, num): # arr은 검색을 할 리스트, num은 찾아야 할 숫자
    global cnt, flag
    l = 0
    r = N - 1

    while l <= r:
        mid = (l+r) // 2
        # A[mid]가 찾는 값일 때
        if arr[mid] == num:
            cnt += 1
            break
        # A[mid]보다 찾는 값이 작을 때는 왼쪽에 있다는 것
        elif arr[mid] > num:
            r = mid - 1
            # 왼쪽으로 한 번 간 적이 있으면
            if flag == -1:
                break
            flag = -1
        # A[mid]보다 찾는 값이 클 때는 오른쪽에 있다는 것
        else:
            l = mid + 1
            # 오른쪽으로 한 번 간 적이 있으면
            if flag == 1:
                break
            flag = 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N은 A에 속한 정수의 개수, M은 B에 속한 정수의 개수

    A = sorted(list(map(int, input().split()))) # A의 숫자
    B = list(map(int, input().split())) # B의 숫자

    cnt = 0 # 정답인 숫자들을 세기 위함
    ans = 0

    for i in B:
        flag = 0  # 좌우 확인
        ans = binary_search(A, i)

    print('#{} {}'.format(tc, ans))
