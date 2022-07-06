import time

#x = int(input()) # 정수 X를 입력 받기
x=10
d = [0] * 30001 # DP 테이블 초기화, 최대 크기 + 1
start_time = time.time()
# 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
for i in range(2, x + 1): # X + 1까지
    d[i] = d[i - 1] + 1 # 현재의 수에서 1을 빼는 경우 리스트 업데이트
    
    if i % 5 == 0: # 현재의 수가 5로 나누어 떨어지는 경우
    	d[i] = min(d[i], d[i // 5] + 1) # 리스트에 작은 수 업데이트
    if i % 3 == 0: # 현재의 수가 3으로 나누어 떨어지는 경우
    	d[i] = min(d[i], d[i // 3] + 1) # 리스트에 작은 수 업데이트
        
    if i % 2 == 0: # 현재의 수가 2로 나누어 떨어지는 경우
    	d[i] = min(d[i], d[i // 2] + 1) # 리스트에 작은 수 업데이트

end_time = time.time()
print("성능 측정:", end_time - start_time)
print(d[x]) # 리스트의 인덱스(입력 숫자) 출력
