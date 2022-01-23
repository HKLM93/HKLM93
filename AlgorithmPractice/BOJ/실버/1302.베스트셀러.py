import sys
input = sys.stdin.readline

N = int(input()) # 오늘 하루 팔린 책의 종류
books = [] # 팔린 책들
for _ in range(N):
    books.append(input().strip())

info = {}
for book in books:
    if book not in info:
        info[book] = 1
    else:
        info[book] += 1

max_count = max(info.values())
best_seller = []

for book, number in info.items():
    if number == max_count:
        best_seller.append(book)

best_seller.sort() # 가장 많이 팔린 책이 여러개일 경우 사전적으로 앞의 책을 출력
print(best_seller[0])