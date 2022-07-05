# 문제 : 퀵 정렬과 병합정렬(파이썬 정렬 라이브러리) 시간 복잡도를 분석하라. 
# 두 알고리즘 모두 빠른 속도를 제공한다. 얼마나 속도가 차이나는가?
# 참고 : 앞서 비교 예제 COMPARISON.py의 소스코드를 사용한다. (랜덤 정수 정렬)
# 범위 : 데이터이 개수를 10000에서 20000, 30000까지 범위를 확장해보자.

from random import randint
import time

# 배열을 무작위 데이터로 초기화 그래프
array = []
for _ in range(30000):
    # 1부터 100 사이의 랜덤한 정수
    array.append(randint(1, 100))

# 퀵 정렬 라이브러리 성능 측정
start_time = time.time()
def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
    	return array
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
#print(quick_sort(array))
# 측정 종료
end_time = time.time()

# 수행 시간 출력
print("퀵 정렬 성능 측정:", end_time - start_time) #퀵 정렬 성능 측정: 0.305905818939209



# 배열을 다시 무작위 데이터로 초기화 그래프
array = []
for _ in range(30000):
    # 1부터 100 사이의 랜덤한 정수
    array.append(randint(1, 100))
    
# 기본 정렬 라이브러리 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

# 측정 종료
end_time = time.time()
# 수행 시간 출력
print("기본 정렬 라이브러리 성능 측정:", end_time - start_time) #기본 정렬 라이브러리 성능 측정: 0.0014052391052246094
