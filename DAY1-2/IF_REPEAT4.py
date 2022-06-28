# DAY1 - 조건문, 반복문
a = input('A, B, C, D 문자에서 1개를 입력 : ')
if (a == "A"): # 문자열 비교
    print("A : best!!!")
elif (a == "B"): # elif는 else if의 약어
    print("B : good!!")
elif (a == "C"):
    print("C : run!")
elif (a == "D"):
    print("D : slowly~")
else:
    print("what?")
    
a=int(input('1~12 사이 숫자 입력하여 월 판단 : '))
if a//3==1: # 3으로 나눠 몫이 1이면 봄(3, 4, 5)
    print("spring")
elif a//3==2: # 3으로 나눠 몫이 2이면 봄(6, 7, 8)
    print("summer")
elif a//3==3: # 3으로 나눠 몫이 3이면 봄(9, 10, 11)
    print("fall")
else: # 아니면 겨울(12, 1, 2)
    print("winter")

#팁(tip) : 파이썬은 나누면 결과는 실수형으로 결과 리턴한다. 
# / 나누기와 다르게 // 나누기는 소수점 이하 X 정수 부분 수만 구함
#round()는 반올림 함수이지만 0.5는 그냥 중간값으로 냅둔다. 예상 외의 답