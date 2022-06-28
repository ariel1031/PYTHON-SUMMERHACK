#  문제 : 중첩된 반복문을 사용하여 구구단을 출력하자.
# • For 문을 중첩, 2단부터 9단까지 출력, 출력 형식 : 2 X 1 = 2

for i in range(2, 10):
    for j in range(1, 10):
        print(i,'x',j,'=',i*j)