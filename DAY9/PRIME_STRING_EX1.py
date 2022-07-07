import math

def is_prime_number(n):
    li=[1]*(n+1)
    for i in range(2, int(math.sqrt(n))+1): #함수 설명 : math.sqrt(x) 함수는 x의 제곱근을 반환합니다. (x에 루트를 씌운 값을 반환)  #출처: https://blockdmask.tistory.com/522 [개발자 지망생:티스토리]
        if li[i]:
            for j in range(i+i, n+1, i):
                li[j]=0
    p=[i for i in range(2, n+1) if li[i]]
    return p

while 1:
    s=input('문자열을 입력하세요 : ')
    max_string=[]
    
    if s=='0':
        break
    p = is_prime_number(100000)
    res = 2
    for n in p:
        if str(n) in s:
            res=n
            max_string.append(res)
    print(max_string)
    print(max(max_string))

# import math

# n = 100000 # 2부터 100000까지의 모든 수에 대하여 소수 판별
# # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)
# primeArr = [True for i in range(n + 1)]

# # 에라토스테네스의 체 알고리즘 수행
# # 2부터 n의 제곱근까지의 모든 수를 확인하며
# for i in range(2, int(math.sqrt(n)) + 1):
#     if primeArr[i] == True: # i가 소수인 경우(남은 수인 경우)
#         # i를 제외한 i의 모든 배수를 지우기
#         j = 2
#         while i * j <= n:
#             primeArr[i * j] = False
#             j += 1

# arr=[]
# s=''
# toFindMax=[]
# while(s!='0'):
#     s = input('문자열을 입력하시오 : ')
#     arr.append(s)

# for i in arr:
#         if primeArr in i :
#             toFindMax.append(i)
# for i in range(len(toFindMax)):            
#     print(toFindMax)