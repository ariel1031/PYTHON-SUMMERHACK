# DAY1 - 조건문, 반복문
a, b, c = input('정수 3개를 입력받아 짝수를 출력 : ').split()
a=int(a)
b=int(b)
c=int(c)

if a%2==0: # 2로 나눠지면 짝수. 짝수 출력
    print(a)
if b%2==0:
    print(b)
if c%2==0:
    print(c)
s = map(int, input('정수 3개를 입력받아 짝수를 출력(for문) : ').split()) #input().split() 결과는 list
for i in s: # s의 첫 요소부터 끝까지 대입 ***i를 굳이 선언하지 않아도 된다. 지역변수로 씀**********************************
    if i % 2 == 0: # 2로 나눠지면 출력
        print(i)
