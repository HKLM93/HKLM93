Nums = set(range(1, 10001))
result = set()

for i in Nums:
    for j in str(i):
        i += int(j) # i는 d(n)이고 j는 생성자
    result.add(i) # 생성자가 있는 숫자들

ans = sorted(Nums-result)

for i in ans:
    print(i)
