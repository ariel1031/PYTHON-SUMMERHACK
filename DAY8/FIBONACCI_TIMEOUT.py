import time
n=10
start_time = time.time()
def Fibonacci(num):
    if num == 0:
	    return 0
    elif num == 2 or num == 1:
    	return 1
    return Fibonacci(num - 2) + Fibonacci(num - 1) # 점화식 표현 중요!
end_time = time.time()
print("성능 측정:", end_time - start_time)
print(Fibonacci(n))