# • 문제 1 : 정수(1 ~ 100) 1개를 입력 받아 1부터 그 수까지 짝수의 합을 출력하시오.
# • for, while 문 선택
# • 문제 2 : 영문 소문자 q가 입력될 까지 입력 문자를 무한 출력하시오.
# • While 문과 if문 활용

#문제 1
a = int(input('정수 1개를 입력 하세요(1~100) : '))
j=0
for i in range(a+1):
    print('i', i)
    if i%2==0:
        j += i
        #print('j', j)
print('j : 짝수의 합', j)

#문제 2
b=''
while(b!='q'):
    b = input('문자 하나를 입력하세요 :')
    print(b)