aeiou = ['a', 'e', 'i', 'o' ,'u' ]

s = list('hegellogo nigicege dagay') #문자열을 한 글자씩 끊어서 리스트로 바꾸기ㄴ
#print(s)

for i in s:
    if i in aeiou:
        #인덱스 반환
        print('i의 인덱스 : ', s.index(i))
        s.(s.index(i)+1)
        print('pop한개 :',s)
        s.pop(s.index(i)+1)
        print('pop두개 :',s)
        print(''.join(s))
