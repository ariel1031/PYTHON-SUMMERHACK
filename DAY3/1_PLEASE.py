import time
import os
import psutil

process = psutil.Process(os.getpid())
start_time = time.time()

#n, k =map(int, input('두 수를 공백으로 분리하여 입력 :').split()) #n,k를 공백을 기준으로 구분하여 입력 받기
n = 64
k = 6
result = 0
while True:
    target = (n//k) * k #k로 나누어 지는 수를 구함
    result += (n-target) #n이 k로 나누어 떨어지는 수가 될 떄까지 빼기 1
    n= target
    if n < k:
        break
    result += 1 #횟수 증가
    n//= k #k로 나누기 n=6
result += (n-1) 
print('1이 도달하기 까지 연산 횟수 :', result)

end_time = time.time()
print("time :", format(end_time - start_time, '.10f'))
print("MB bytes :",process.memory_info().rss / (1024.0 * 1024.0))