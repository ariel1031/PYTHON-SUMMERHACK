n = int(input('NxN 2차원 행렬을 생성(N 입력): '))
plans = input('L,R,U,D 4가지 방향 이동 계획 입력 : '.split())
x, y = 1, 1

dx = [0,0,-1,1]
dy = [1,-1,0,0]

move_types = ['R', 'L','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
        
    x, y =nx, ny

print('모험가 최종 좌표 : ', x, y)