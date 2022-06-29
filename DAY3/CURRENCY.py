import time
import os
import psutil

process = psutil.Process(os.getpid())
start_time = time.time()

n = 1260
#n = int(input('거스름돈을 가격(정수)로 입력해주세요 :'))
#가격 입력을 받기 위해 정수 캐스팅
count = 0

array = [500,100,50,10] #큰 단위의 화폐부터 차례대로 확인하기
for coin in array:
    count += n // coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print('동전의 거스름돈 최소 개수는 :', count) #개수 결과 출력

end_time = time.time()
print("time :", format(end_time - start_time, '.10f'))
print("MB bytes :",process.memory_info().rss / (1024.0 * 1024.0))