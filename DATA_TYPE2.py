# 자료형
a = "Hello"
b = "World"
print(a + " " + b) # +은 문자를 연결 출력, 분리할때는 split()
c = "String"
print(c * 3) # *은 문자를 반복 연결 출력
d = "ABCDEF"
print(d[2 : 4]) # 인덱스/슬라이싱 2번~4번 문자 출력. 출력은 인덱스 2-3까지만 나옴
print(d[2:]) # 생략 가능, 3번~끝 문자 출력
print(d[:5]) # 생략 가능, 시작부터~5번 문자 출력
print('d[2:-2]', d[2:-2]) #CD
print('d[:-1]', d[:-1]) #d[:-1] ABCDE
print('d[:]', d[:])
#d[1] = 'i' d[0:3] = "1234" 직접 수정 불가

#구현할 시간이 없으니 기억하고 시간 단축할 함수들
str_length = len(d) # 문자열 길이
str_min = min(d) # 문자열 중 작은 값
str_max = max(d) # 문자열 중 큰 값
str_count = d.count('B') # 문자열 내 B의 개수
print(str_length)
print(str_min)
print(str_max)
print(str_count)
print(d.find('C')) # 문자열 내 C의 위치
