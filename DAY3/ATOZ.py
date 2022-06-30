s = input('문자열을 입력하세요 : ')
pos = 'abcdefghijklmnopqrstuvwxyz'

for i in pos:
    if i in s:
        print(i, s.index(i), end=' ')
    else:
        print(i, -1, end = ' ')