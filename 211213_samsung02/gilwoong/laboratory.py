# 백준 14502 '연구소'
# https://www.acmicpc.net/problem/14502

from collections import deque
from copy import deepcopy

def dfs(cnt, idx):
    global N, M, MAP, virus_list, empty_list, answer, di, dj
    
    if cnt == 3:
        que = deque()
        for i, j in virus_list:
            que.append((i, j))
        
        tmp_map = deepcopy(MAP)
        while que:
            i, j = que.popleft()

            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                if not (0 <= ni < N and 0 <= nj < M):
                    continue

                if tmp_map[ni][nj] == 0:
                    tmp_map[ni][nj] = 2
                    que.append((ni, nj))
        
        safe_area = 0
        for i in range(N):
            for j in range(M):
                if tmp_map[i][j] == 0:
                    safe_area += 1
        
        answer = max(answer, safe_area)
        return
            
        
    for k in range(idx + 1, len(empty_list)):
        i, j = empty_list[k]
        MAP[i][j] = 1
        dfs(cnt + 1, k)
        MAP[i][j] = 0
    
    return
    

N, M = map(int, input().split())
MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().split())))

virus_list = []
empty_list = []
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 2:
            virus_list.append((i, j))
        elif MAP[i][j] == 0:
            empty_list.append((i, j))

answer = 0

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
dfs(0, -1)

print(answer)
