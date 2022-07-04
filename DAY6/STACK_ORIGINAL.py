stack = []

stack.append(4)
stack.append(8)
stack.append(6)
stack.append(1)
stack.append(3)
stack.append(7)
print(len(stack))
stack.pop()
stack.append(8)
stack.append(5)
stack.pop()

print(stack[::-1]) #[8, 3, 1, 6, 8, 4] 역순으로 전부 나오네
print(stack) #[4, 8, 6, 1, 3, 8]

#그냥 stack이라는 이름으로 list 만든거임