adj = [
    [0 for _ in range(8)] for _ in range(8)
]

adj[1][2] = 1
adj[1][3] = 1
adj[2][5] = 1
adj[3][7] = 1
adj[4][2] = 1
adj[4][6] = 1
adj[5][6] = 1
adj[6][4] = 1
adj[7][3] = 1
adj[7][6] = 1

from collections import deque

def bfs(start):
    queue = deque()
    visited = [0 for _ in range(8)] # 1또는0 큐에 재등록 방지

    queue.append(start)
    visited[start] = 1 # 큐에 재등록 방지

    while queue : # 방문 예약 있을때
        now  = queue.popleft()
        # 탐색
        print("{} level : {}".format(now, visited[now] - 1))
        for next in range(1,8): # 연결되있는 노드 큐에 등록 (방문 예약 )
            if adj[now][next] == 0 : continue
            if visited[next] > 0 : continue
            visited[next] = visited[now] + 1 # 큐에 재등록 방지
            queue.append(next)

bfs(1)