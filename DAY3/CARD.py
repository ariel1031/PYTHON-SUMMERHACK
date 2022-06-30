#행을 기준으로 순차 선택 , 첫 뽑기는 반드시 가장 작은 카드를 한개 뽑아야한다
#그니까 말이야 ~~~~~~ 짜근 애들 중 제일 큰걸 골라라

N, M = map(int, input('행, 열 입력하세요: ').split())
maximum = 0

for i in range(N):
    data =  list(map(int, input('행 값 입력 : ').split()))
    minimum = min(data)
    maximum = max(maximum, minimum)

print(maximum)    

    

#list = [0 for i in range(5)] #[0, 0, 0, 0, 0]