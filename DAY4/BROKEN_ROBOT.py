direction_num = {'N': 0, 'E': 1, 'S': 2, 'W':3, 0:'N', 1:'E', 2:'S', 3:'W'} # NWSE 방향 번호 정의, 양방향
direction_to_position = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W':(0, -1)} # 이동 좌표정의 : X가 0이 아님(-1) 
 
def find_direction(start, command, repeat): # 
    repeat %= 4 # 4의 배수는 1바퀴이므로 같은 방향을 가르킴
    start_num = direction_num[start] # 시작번호를 받아와서
    # 방향에 맞춰 돌려본다.
    if command == 'L':
        start_num-=repeat
        # 0보다 적어지면 보정
        if start_num < 0: start_num += 4 # 원위치
    # 반대도 마찬가지
    else:
        start_num+=repeat
        if start_num > 3: start_num -= 4 # 반대
    return direction_num[start_num]
answer = None
A, B = map(int, input('A X B 맵의 크기를 입력 : ').split()) # 5 4 맵 크기 입력 받음
field = [[0 for _ in range(A)] for _ in range(B)] # 5X4 행열 맵 생성
robots = [0] # 0번 인덱스는 사용 X(임시번호), 로봇 1~N번 사용
N,M = map(int, input('로봇의 개수, 명령의 개수 입력 : ').split()) # 2개 로봇, 2개 명령
for i in range(N): # 예) 2번째 로봇 기준 설명
    x, y, direction = input('로봇의 좌표 x,y 와 방향 입력 : ').split() # 두번째 로봇의 좌표와 방향 5, 4, W
    x, y = int(x)-1, int(y) # 좌표 보정 -1, X축 인덱스 0번 부터 시작 되기 때문 : 두번째 로봇 좌표와 방향 4, 4, W
    robots.append([B-y, x, direction])# 좌표 보정, Y축의 뒤집음(아래부터 시작) : 두번째 로봇 정보 추가 0, 4, W
    print('추가된 로봇 정보 출력:', robots)
    field[B-y][x] = i+1 # [0][4] 위치에 두번째 로봇 체크 2
    print('맵에 추가된 로봇을 체크 : ', field)
for i in range(M):
    idx, command, repeat = input('로봇 번호, 이동 명령, 횟수 입력 :').split() # 로봇번호 2, 명령어 F, 횟수 7
    idx, repeat = int(idx), int(repeat) # 정수 캐스팅
    y, x, direction = robots[idx] # 4, 0, F
    print('로봇 번호, 명령어, 횟수 입력 중간 값 디버깅 : ', y, x, direction )
    if command == 'F': # 전진일때 처리 2번 로봇 F이동 시작
        dy, dx = direction_to_position[direction] # 이동위치에 필요한 값 0, -1
        for i in range(repeat): # 이동해야 하는 횟수만큼 반복
            move_y, move_x = y+dy, x+dx # 이동할 좌표를 계산하고
            if 0 <= move_y < B and 0 <= move_x < A: # 맵밖으로 벗어나지 않았다면 동작 3번정도 이동
                # 이동하는 위치에 로봇이 있다면 충돌처리
                if field[move_y][move_x]:
                    answer = 'Robot {} crashes into robot {}'.format(idx, field[move_y][move_x])
                    break
                # 이동이 가능하고 이동할 위치에 아무것도 없다면
                else:
                    field[y][x]=0 # 현재위치에 정보를 없애고
                    field[move_y][move_x] = idx # 이동위치에 로봇정보를 표시하고
                    y, x = move_y, move_x # 현재 정보를 이동한 위치정보로 갱신
                    robots[idx] = [move_y, move_x, direction] # 로봇의 정보또한 마찬가지로 갱신
# 맵 밖으로 나갔다면 밖으로 나갔다고 정답 갱신하기
            else: # 7번 앞으로 이동 -1하게 되면 맵 좌표에서 벗어남
                answer = 'Robot {} crashes into the wall'.format(idx)
                break
    
    else: # L, R 회전일때 처리
        robots[idx][2] = find_direction(direction, command, repeat) # 현재보는 방향과 명령과 횟수를 전달하여 정보갱신
    if answer: break # 정답이 존재하면 충돌
        
if not answer: answer = 'OK' # 정답이 비어있다면 통과로 변경해주기
print(answer)

