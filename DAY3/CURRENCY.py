import time
import os
import psutil

process = psutil.Process(os.getpid())
start_time = time.time()

#n = int(input('거스름돈을 가격(정수)로 입력해주세요: '))
#가격 입력을 받기 위해 정수 캐스팅

n,k = map(int, input('거스름돈 화폐의 종류 수(n)와 돈의 가격(k) 입력 : ').split())
Ai=[]
for _ in range(n):
    Ai.append(int(input('거스름돈 단위를 거스름돈 화폐의 종류 수 만큼 입력해주세요: ')))

Ai.sort(reverse=True)
print('reversed Ai : ',Ai)

count = 0
for coin in Ai:
    count += k // coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    print('count += k // coin', count)
    k %= coin
    print('k %= coin',k)

print('동전의 거스름돈 최소 개수는 :', count) #개수 결과 출력

end_time = time.time()
print("time :", format(end_time - start_time, '.10f'))
print("MB bytes :",process.memory_info().rss / (1024.0 * 1024.0))