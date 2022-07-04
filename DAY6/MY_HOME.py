def DFS(x,y,L):
    dx = [-1, 0, 1, 0] # 4가지 방향 정의
    dy = [0, 1, 0, -1]
    for i in range(4): # 상하좌우 검사
        nx = x+dx[i]
        ny = y+dy[i]
        
        if 0<=nx<n and 0<=ny<n and arr[nx][ny]==1: # 새로운집 발견
            arr[nx][ny]=0
            cnt_arr[L]+=1 # 다음 좌표 설정
            DFS(nx,ny,L) # DFS 재귀 호출
n = int(input('단지의 크기 N를 입력 : '))
arr = [list(map(int,input('단지 지도 세부 정보를 입력 : '))) for _ in 
range(n)]
total_cnt = 0 # 단지의 숫자
cnt_arr=list() # 단지안에 속하는 집의 수

for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            arr[i][j]=0
            cnt_arr.append(1) # 초기 방문 표시
            DFS(i,j,total_cnt) # DFS 탐색 시작
            total_cnt += 1
print('총 단지수 :', total_cnt)
cnt_arr.sort()
for i in cnt_arr:
    print('각 집의 개수 :', i)
