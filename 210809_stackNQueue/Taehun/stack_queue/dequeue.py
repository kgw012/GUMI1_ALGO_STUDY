from collections import deque

queue = deque()
queue.append(3)
queue.append(2)
queue.append(1)
queue.append(5)
queue.append(7)
ret = queue[0] #peek
ret = queue.popleft() # peek + dequeue

while queue:
    ret = queue.popleft()
    print(ret, end = ' ')


#Dequeue : 큐에서 제거
#Decqueue : 자료구조의 일종
# 내가 구현

# queue = [3,7,2,1,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# front = 0
# rear = 5
#
# while (front < rear):
#     print(queue[front])
#     front += 1
#
# print(rear, front)