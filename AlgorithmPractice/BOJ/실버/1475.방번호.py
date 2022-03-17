import sys
input = sys.stdin.readline

N = input().strip() #N은 만들어야 할 숫자

num_set = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0} # 6은 9로 바꿀 수 있어서

for idx in range(len(N)):
    if N[idx] in ['6', '9']:
        num_set['6'] += 1 # 6하고 9가 같아서
    else:
        num_set[N[idx]] += 1

if num_set['6'] % 2 == 0:
    num_set['6'] = num_set['6'] // 2
else:
    num_set['6'] = num_set['6'] // 2 + 1

print(max(num_set.values()))