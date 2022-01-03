# 백준 21608 '상어 초등학교'
# https://www.acmicpc.net/problem/21608

from sys import stdin

N = int(stdin.readline())
input_list = list()
for _ in range(N*N):
    input_list.append(list(map(int, stdin.readline().split())))

MAP = [[0] * N for _ in range(N)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

std_dict = dict()

for lst in input_list:
    std = lst[0]
    fav_lst = lst[1:5]

    std_dict[std] = fav_lst

    res_lst = []

    for i in range(N):
        for j in range(N):
            if MAP[i][j] != 0:
                continue
            
            res = [0, 0, 0, 0]

            fav_cnt = 0
            empty_cnt = 0

            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                if not (0 <= ni < N and 0 <= nj < N):
                    continue
                
                # condition 2
                if MAP[ni][nj] == 0:
                    empty_cnt += 1
                    continue
                
                # condition 1
                if MAP[ni][nj] in fav_lst:
                    fav_cnt += 1
                
            
            res[0] = -fav_cnt       # condition 1
            res[1] = -empty_cnt     # condition 2
            res[2], res[3] = i, j   # condition 3
            res_lst.append(res)
    
    res_lst.sort()

    i, j = res_lst[0][2], res_lst[0][3]
    MAP[i][j] = std

score = 0
for i in range(N):
    for j in range(N):
        std = MAP[i][j]
        fav_lst = std_dict[std]

        cnt = 0
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if not (0 <= ni < N and 0 <= nj < N):
                continue
            
            if MAP[ni][nj] in fav_lst:
                cnt += 1
        
        if cnt == 0:
            continue
        else:
            score += 10**(cnt - 1)

print(score)
