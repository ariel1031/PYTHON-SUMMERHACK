# 데이터의 개수 N과 데이터 입력받기
n, m = map(int,input('데이터 개수, 합 : '))
data = list(map(int, input('데이터를 입력하시오 : ').split()))

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
        # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]
print(count)
