import time
import os
import psutil

process = psutil.Process(os.getpid())
start_time = time.time()

# H 입력 받기
#h = int(input('1시~23시 사이 시간 입력 : '))
h=13
count = 0
for i in range(h + 1): # 시간 
    for j in range(60): # 분
        for k in range(60): # 초
            if '3' in str(i) + str(j) + str(k): # 매 시각 안에 '3'이 포함되어 있다면 
                count += 1 # 카운트 증가
        print(count)
print('최종 3이 카운트 된 결과는 :', count)

end_time = time.time()
print('time : ', format(end_time - start_time, '.10f'))
print('MB bytes : ', process.memory_info().rss / (1024.0 *1024.0))