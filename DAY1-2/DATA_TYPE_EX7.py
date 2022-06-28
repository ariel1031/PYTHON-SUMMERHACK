# • 문제 : 리스트에 문자열을 저장하고 출력
# • 리스트 [] 선언, append 함수(내용 추가) 활용
# • While문 내에서 입력 받기 : if 스페이스( ‘ ‘ ) 누르면 정지
# • 리스트 컴프리핸션 전체 출력 : for문

list = []
while(1):
    str = input('문자열을 입력하시오 :') 
    if str=='':
        break
    list.append(str)
    
for i in list:
    print(i, end=' ')