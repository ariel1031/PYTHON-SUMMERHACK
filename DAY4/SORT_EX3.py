# • 문제 : 코딩테스트 회원으로 가입한 사람의 나이와 이름은 순서대로
# 저장된다. 회원들의 나이순으로 정렬하는 출력하는 프로그램을 작성하시오.
# • 참고 : 나이가 같으면 먼저 가입한 사람이 앞에 온다.
# • 요구사항 : 시간 제한 1초, 메모리 제한 128MB

#람다, 소티드
# https://velog.io/@aonee/Python-%EC%A0%95%EB%A0%AC-sort-sorted-reverse

#기본 방식 1(람다 키 사용)
n_members = int(input('회원의 인원 : '))
member_list = []

for _ int range(n_members):
    (x, y) = input('나이와 이름을 공백으로 입력 받습니다.').split()
    member_list.append((int(x), y)) 
    
sorted_list = sorted(member_list, key=lambda x:x[0]) #정렬하는 키 기준이 이스트의 첫번째 값

for i in sorted_list:
    print(i[0],i[1])