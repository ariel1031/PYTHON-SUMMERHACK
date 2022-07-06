# DP 메모제이션 기법으로 피보나치 구현
#dinamic programming : 임시공간 만들기, 점화식 추론해서 작성하기, 재귀호출

import time
import sys

# n = int(sys.stdin.readline()) 더 빠른 입력 방식
#N = int(input()) # 실행 해 본 후 n을 30~50정도로 테스트

N=100000

start_time = time.time()

#dinamic table : 임시공간 만들기
arr = [0 for _ in range(N+1)] # 임시 공간 리스트 생성, 초기화 

arr[1] = 1 # 0, 1로 시작

#점화식 추론해서 작성, 재귀호출
for i in range(2, N+1): # 피보나치 2부터 유효
	arr[i] = arr[i-1] + arr[i-2] # 바로 값을 가져옴
    
end_time = time.time()
print("성능 측정:", end_time - start_time)
print(arr[-1])
