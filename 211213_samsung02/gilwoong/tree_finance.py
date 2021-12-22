# 백준 16235 '나무 재테크'
# https://www.acmicpc.net/problem/16235

import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, M, K = map(int, input().split())

    food_map = []
    for _ in range(N):
        food_map.append(list(map(int, input().split())))
    
    MAP = [[{
                'tree_dict': dict(),
                'food': 5,
                'tree_to_food': 0,
            } for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        x, y, z = map(int, input().split())
        MAP[x - 1][y - 1]['tree_dict'][z] = 1
    
    for k in range(K):
        tmp_dict = [[dict() for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                # spring
                plus_tree_cnt = 0
                for age, cnt in sorted(MAP[i][j]['tree_dict'].items()):
                    plus_cnt = min(MAP[i][j]['food'] // age, cnt)
                    if plus_cnt > 0:
                        MAP[i][j]['food'] -= age*plus_cnt
                        if (age + 1) not in tmp_dict[i][j]:
                            tmp_dict[i][j][age + 1] = 0
                        tmp_dict[i][j][age + 1] += plus_cnt

                        if (age + 1) % 5 == 0:
                            plus_tree_cnt += plus_cnt
                    
                    MAP[i][j]['tree_to_food'] += (age // 2) * (cnt - plus_cnt)
                
                # summer
                MAP[i][j]['food'] += MAP[i][j]['tree_to_food']
                MAP[i][j]['tree_to_food'] = 0

                # autumn
                if not plus_tree_cnt:
                    continue

                st_i = max(i - 1, 0)
                st_j = max(j - 1, 0)
                fn_i = min(i + 1, N - 1)
                fn_j = min(j + 1, N - 1)

                for ni in range(st_i, fn_i + 1):
                    for nj in range(st_j, fn_j + 1):
                        if i == ni and j == nj:
                            continue
                        if 1 not in tmp_dict[ni][nj]:
                            tmp_dict[ni][nj][1] = 0
                        tmp_dict[ni][nj][1] += plus_tree_cnt
        
        # winter
        for i in range(N):
            for j in range(N):
                MAP[i][j]['food'] += food_map[i][j]
        
        # tmp_dict -> MAP
        for i in range(N):
            for j in range(N):
                MAP[i][j]['tree_dict'] = tmp_dict[i][j]

    # result
    answer = 0
    for i in range(N):
        for j in range(N):
            answer += sum(MAP[i][j]['tree_dict'].values())
    print(answer)
