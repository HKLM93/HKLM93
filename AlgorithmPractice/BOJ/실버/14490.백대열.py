import sys
# 최대공약수를 구하기 위한 라이브러리
from math import gcd
input = sys.stdin.readline

number = input().split(':')
n, m = int(number[0]), int(number[1])

gdc_num = gcd(n, m)

print(f'{n//gdc_num}:{m // gdc_num}')


