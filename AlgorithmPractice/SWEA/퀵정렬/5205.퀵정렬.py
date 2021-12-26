import sys
sys.stdin = open('sample_input.txt', 'r')

# 1. hoare_p
def partition(arr, l, r):
    # 피봇설정(리스트의 첫번째 값)
    pivot = arr[l]
    # 인덱스(리스트의 첫번째 값과 마지막 값의 인덱스 = 0과 리스트의 길이)
    i, j = l, r

    while i <= j:
        # 왼쪽 인덱스가 바라보는 값이 피봇값보다 작거나 같을 때(피봇값보다 큰 값을 찾기 위함)
        while i <= j and arr[i] <= pivot:
            # 왼쪽 인덱스 +1
            i += 1
        # 오른쪽 인덱스가 바라보는 값이 피봇값보다 크거나 같을 때(피봇값보다 작은 값을 찾기 위함)
        while i <= j and arr[j] >= pivot:
            # 오른쪽 인덱스 -1
            j -= 1
        # 피봇값보다 큰 값과 작은 값을 찾았을 때
        if i < j:
            # 둘의 위치 바꿔주기
            arr[i], arr[j] = arr[j], arr[i]
    # i와 j가 교차하는 곳이 피봇값이 위치해야하는 곳
    arr[l], arr[j] = arr[j], arr[l]
    # 피봇값은 자기 위치로 갔기 때문에 정렬을 계속하기 위해 피봇값이 들어간 인덱스보다 1이 작은 j를 출력
    return j

##############################################################################
# 2. lomuto p

def lomuto_p(A, l, r):
    pivot = A[r]
    i = l-1

    for j in range(l, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]

    return i+1

def quick_sort(arr, l, r):
    if l < r:
        # j를 받음
        # s = partition(arr, l, r)
        s = lomuto_p(arr, l, r)
        # j를 기준으로 왼쪽 리스트를 다시 정렬
        quick_sort(arr, l, s-1)
        # j를 기준으로 오른쪽 리스트를 다시 정렬
        quick_sort(arr, s+1, r)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, len(arr)-1)

    print('#{} {}'.format(tc, arr[N//2]))



