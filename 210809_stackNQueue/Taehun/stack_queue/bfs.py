from collections import deque

value = [0,1,1,3,2,4,5,2]
adj = [
    [0 for _ in range(8)] for _ in range(8)
]
# from -> to [from][to]
adj[0][1] = 1
adj[0][2] = 1
adj[0][3] = 1
adj[1][4] = 1
adj[1][5] = 1
adj[1][6] = 1
adj[3][7] = 1

# 내가 구현
queue = deque()
queue.append(0)
while(queue):
    now = queue.popleft()
    print(value[now], end= ' ')

    for next in range(8):
        if adj[now][next] == 1:
            queue.append(next)




# 교수님 ans
# queue = deque()
# queue.append(0) # 시작노드 큐등록
#
# #BFS
# while queue : # 방문 예약 있다!
#     now = queue.popleft()
#     # 방문 / 탐색
#     print(now, end = ' ')
#
#     for next in range(8):
#         if adj[now][next] == 1:
#             queue.append(next) ## 자식노드 찾아서 큐등록(방문예약 )