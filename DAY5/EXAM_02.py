serialNum = list(input('주민등록 번호를 입력하시오 : '))
mon = int(serialNum[2]+serialNum[3]) 
day = int(serialNum[4]+serialNum[5])
gen = int(serialNum[7])
region = int(serialNum[8]+serialNum[9])

if (1 <= mon and mon <= 12) and (1 <= day and day <= 31) and (1 <= gen and gen <= 4):
    print('유효한 주민등록 번호입니다.')
    if gen == '1' or gen =='3':
        print('성별 : 남성')
    else:
        print('성별 : 여성')
    
    ##sudo 코드
    #지역별로 서울 경기 등을 출력
    
    
else:
    print('유효한 주민등록 번호를 입력해주세요.')