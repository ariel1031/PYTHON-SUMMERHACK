s = list(input('숫자를 입력하세요 : '))
while(len(s) < 2):
    print("두 자리 이상의 숫자를 입력하세요")
    s = list(input('숫자를 입력하세요 : '))
    
x = int(input('몇 개씩 끊을까요 : '))
while(x<1):
    print('1 이상의 자연수를 입력해주세요')
    x = int(input('몇 개씩 끊을까요 : '))

maximum = 0

sudo코드
s는 list 이므로 x만큼의 숫자를 제거하는 방법을
#s[0],s[1] # s[0],s[2] # s[0],s[3]
#s[1],s[2] # s[1],s[3]
#s[2],s[3]
이런 식으로 s에서 특정 인덱스들만 삭제하고
for 문에서  x 개 만큼 숫자를 제거한 수를 넘겨 줘서
현재의 maximum과 max함수로 비교하여 큰 쪽을 maximum으로 업데이트 한다.
