# 문자열 뒤집기 1
letters = '삼성청년소프트웨어아카데미'
s = list(letters)

l = len(s)

for i in range(l//2):
    s[i], s[l - 1 -i] = s[l - 1 -i], s[i]
ans = str(''.join(s))
print(ans)

# 문자열 뒤집기 2
letters = '삼성청년소프트웨어아카데미'
s = list(letters)

for i in range(len(s)-1, -1, -1):
    print(s[i], end ='')
print()

# 문자열 뒤집기 3
print(letters[::-1])

# 문자열 뒤집기 4
print(''.join(reversed(letters)))
