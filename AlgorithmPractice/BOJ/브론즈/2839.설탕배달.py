import sys
input = sys.stdin.readline

sugar = int(input())
cnt = 0 # 봉지의 개수

while sugar >= 0:
    if sugar % 5 == 0:
        cnt += (sugar//5)
        print(cnt)
        break
    sugar -= 3
    cnt += 1

# 정확하게 사지 못하면
else:
    print(-1)
