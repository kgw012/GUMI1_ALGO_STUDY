from collections import deque

adj = [
    [0 for _ in range(5)] for _ in range(5)
]

adj[0][1] = 1
adj[0][2] = 1
adj[1][3] = 1
adj[1][4] = 1
adj[2][1] = 1
adj[2][3] = 1
adj[4][2] = 1

queue = deque()
queue.append(0)
visited = [0 for i in range(5)]
while(queue):
    now = queue.popleft()
    print("{}의 level은 {}".format(now, visited[now]))
    for next in range(5):
        if adj[now][next] == 1 and visited[next] == 0:
            queue.append(next)
            # 큐에 재등록 방지 + level 같이 저장
            visited[next] = visited[now] + 1
