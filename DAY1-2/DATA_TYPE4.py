#2차원 정방 행렬
# 자료형
n = 4
m = 3
array = [[0] * m for _ in range(n)] # N X M 크기의 2차원 행렬 **************************
#리스트 초기화 : 대괄호, 리스트 컴프리헨션
print(array)
print(type(array)) # 현재 자료구조 타입 확인

array[2][1] = 5
print(array)

a = [1, 4, 3]
print("기본 리스트: ", a)

a.append(2) # 리스트에 원소 삽입
print("삽입: ", a)

a.sort() # 오름차순 정렬
print("오름차순 정렬: ", a)

a.sort(reverse = True) # 내림차순 정렬
print("내림차순 정렬: ", a)

a.insert(2, 3) # 특정 인덱스에 데이터 추가
print("인덱스 2에 3 추가: ", a)

print("값이 3인 데이터 개수: ", a.count(3)) # 특정 값인 데이터 개수 세기

a.remove(1) # 특정 값 데이터 삭제
print("값이 1인 데이터 삭제: ", a)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5} # ****************특정 원소 모두 제거, 집합 자료형 활용*************
result = [i for i in a if i not in remove_set] # remove_list에 포함되지 않은 값만을 저장
print(result)

# ###########다음은 다른 immutable 타입인 문자열(string)과 튜플( tuple)의 예이다.

# >>>   x = 'abcd'
# >>>   y = x
# >>>   y += 'e'
# >>>   x
# abcd
# >>> y
# abcde
