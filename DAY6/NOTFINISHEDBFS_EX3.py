from collections import deque # 큐 자료구조 연동
n = int(input('단지의 크기 N를 입력 : '))
arr = [list(map(int,input('단지 지도 세부 정보를 입력 : '))) for _ in 
range(n)]
cnt = 0 # 단지의 숫자
cnt_arr=list() # 단지안에 속하는 집의 수

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = queue()