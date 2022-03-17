import sys
sys.stdin = open('input.txt', 'r')

# 가로줄 확인
def row_count(nums):
    total = 0
    for i in range(len(nums)):
        Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        cnt = 0
        for j in range(len(nums[i])):
            if nums[i][j] in Numbers:
                # 1-9까지 있는 리스트에서 스도쿠의 가로 줄에 있는 숫자가 있으면 지워나감.
                Numbers.remove(nums[i][j])
                cnt += 1
            else:
                return False
        # 1줄이 모두 확인
        if cnt == 9:
            total += 1
    # 9줄 모두 확인
    if total == 9:
        return True
    else:
        return False

# 세로줄 확인
def col_count(nums):
    total = 0
    for j in range(len(nums[0])):
        Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        cnt = 0
        for i in range(len(nums)):
            if nums[i][j] in Numbers:
                # 1-9까지 있는 리스트에서 스도쿠의 세로 줄에 있는 숫자가 있으면 지워나감.
                Numbers.remove(nums[i][j])
                cnt += 1
            else:
                return False
        # 1줄이 모두 확인
        if cnt == 9:
            total += 1
    # 9줄 모두 확인
    if total == 9:
        return True
    else:
        return False

# 3x3 확인
def square_count(nums):
    total = 0
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            cnt = 0
            for k in range(3):
                for l in range(3):
                    if nums[i+k][j+l] in Numbers:
                        # 1-9까지 있는 리스트에서 스도쿠의 세로 줄에 있는 숫자가 있으면 지워나감.
                        Numbers.remove(nums[i+k][j+l])
                        cnt += 1

            # 1칸이 모두 확인
            if cnt == 9:
                total += 1
    # 9칸 모두 확인
    if total == 9:
        return True
    else:
        return False

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    if row_count(arr) and col_count(arr) and square_count(arr):
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))




