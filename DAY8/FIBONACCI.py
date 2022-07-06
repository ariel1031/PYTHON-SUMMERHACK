# 피보나치 함수(Fibonacci Function)을 재귀함수로 구현
# -> 개선이 필요하다. 타임아웃될 확률이 높음
def fibo(x):
	if x == 1 or x == 2:
		return 1
	return fibo(x - 1) + fibo(x - 2)

print(fibo(17))
# 단순 재귀 함수 구현 → 지수 시간 복잡도(10억 이상)
