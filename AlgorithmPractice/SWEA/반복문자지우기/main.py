import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    test_case = list(input())

    while True:
        for i in range(len(test_case)-1):
            if test_case[i] == test_case[i+1]:
                test_case.pop(i+1)
                test_case.pop(i)
                break
        else:
            break
    result = len(test_case)

    print('#{} {}'.format(tc, result))

