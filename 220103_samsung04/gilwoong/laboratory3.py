# 백준 17142 '연구소3'
# https://www.acmicpc.net/problem/17142

from collections import deque
from sys import stdin

input = stdin.readline

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def dfs(N, M, MAP, virus_list, empty_cnt, select_list, cnt, idx):
    if cnt >= M:
        visits = [[False] * N for _ in range(N)]

        que = deque()
        for k in select_list:
            i, j = virus_list[k]
            que.append((i, j, 0))
            visits[i][j] = True
        
        level = 0
        cnt = 0
        while que:
            i, j, level = que.popleft()

            if cnt >= empty_cnt:
                break

            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                if not (0 <= ni < N and 0 <= nj < N):
                    continue
                
                if visits[ni][nj]:
                    continue
                
                if MAP[ni][nj] == 1:
                    continue
                
                if MAP[ni][nj] == 0:
                    cnt += 1

                visits[ni][nj] = True
                que.append((ni, nj, level + 1))
        
        if cnt == empty_cnt:
            if que:
                level = que[-1][2]
            return level

        return N * N

    answer = N * N
    for k in range(idx + 1, len(virus_list)):
        select_list[cnt] = k
        answer = min(answer, dfs(N, M, MAP, virus_list, empty_cnt, select_list, cnt + 1, k))
    
    return answer


if __name__ == '__main__':
    N, M = map(int, input().split())
    MAP = []
    for _ in range(N):
        MAP.append(list(map(int, input().split())))
    
    virus_list = []
    empty_cnt = 0

    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 2:
                virus_list.append((i, j))
            if MAP[i][j] == 0:
                empty_cnt += 1
    
    select_list = [0] * M
    answer = dfs(N, M, MAP, virus_list, empty_cnt, select_list, 0, -1)

    if answer == N * N:
        answer = -1
    
    if empty_cnt == 0:
        answer = 0

    print(answer)
