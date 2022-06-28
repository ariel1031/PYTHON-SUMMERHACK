a.insert(2, 3) # 특정 인덱스에 데이터 추가
print("인덱스 2에 3 추가: ", a)

print("값이 3인 데이터 개수: ", a.count(3)) # 특정 값인 데이터 개수 세기

a.remove(1) # 특정 값 데이터 삭제
print("값이 1인 데이터 삭제: ", a)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5} # 특정 원소 모두 제거, 집합 자료형 활용*****
result = [i for i in a if i not in remove_set] # remove_list에 포함되지 않은 값만을 저장
print(result)