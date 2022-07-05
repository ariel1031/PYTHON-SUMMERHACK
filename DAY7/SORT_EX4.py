from bisect import bisect_left, bisect_right
from random import randint
import time

n,x = list(map(int, input('숫자를 몇 개 입력 받을래? 그리고 숫자는 뭘 찾을래?? : ').split()))
arr = list(map(int,input('원소를 입력하세요 : ').split()))

# 이진탐색 프로그램 성능 측정
start_time = time.time()
arr.sort()

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

end_time = time.time()
print("이진탐색 성능 측정:", end_time - start_time)

# 값이 4인 데이터 개수 출력
print(count_by_range(arr, 137, 137))

