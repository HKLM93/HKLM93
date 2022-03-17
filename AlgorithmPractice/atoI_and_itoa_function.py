# atoi 함수 - 숫자 문자열을 int로
def atoi(str_input: str) -> int: 
    ans =0

    for i in range(len(str_input)):
        ans *= 10
        ans += ord(str_input[i]) - ord('0')
        # 또는 ord(str_input[i]) -48 도 가능

    return ans

# itoa 함수 - int를 숫자 문자열로
def itoa(int_input: int) -> str:
    ans = ''
    tmp = int_input
    
    # 이와 같이 작성했다면 뒤집어서 결과가 나온다(뒤집는 방법은 많다)
    while tmp >0:
        num = tmp % 10
        ans += chr(num + 48) #아스키코드 변환 방법
        tmp //= 10
    
    return ans[::-1]



