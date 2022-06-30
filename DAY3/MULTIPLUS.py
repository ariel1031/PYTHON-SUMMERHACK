data =input('0~9 숫자로 이루어진 문자열 입력 :')
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    print('num : ', num)
    if num <=1 or result <=1:
        result += num
    else:
        result *= num
        
print('최종 연산 결과 합산된 수의 크기는 : ', result)