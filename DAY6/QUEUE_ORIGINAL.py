#큐보다 디큐가 효율적이라고 한다.

from collections import deque
queue = deque()

queue.append(4)
queue.append(1)
queue.append(3)
queue.append(7)
queue.popleft()

print(queue)
queue.append(6)
queue.append(0)
queue.popleft()
print(queue)
queue.reverse() #나중에 들어온 순서대로 역정렬
print(queue)
print(type(queue))