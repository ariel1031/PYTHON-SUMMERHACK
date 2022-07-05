# • 문제 : 큰 수부터 작은 수 순서로 정렬하는 프로그램을 작성하라. 
# • 참고 : 입력 : 첫번째 줄에 수열에 속해 있는 수의 개수 N, 
#   두번째 줄부터 N+1 번째줄에는 N개의 수를 모두 입력. 범위는 1이상 10만 이하의 자연수
# • 참고 : 공백 구분, 중복되는 수의 처리 상관없음
# • 요구사항 : 시간 제한 1초, 메모리 제한 128MB

arr=[]
n = int(input('몇 개 입력할거니 : '))
for i in range(n):
    a = int(input('숫자를 입력해 주세요 : '))
    arr.append(a)


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

print(quick_sort(arr))