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
        tmp_map = [[dict()] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                # spring
                for age, cnt in sorted(MAP[i][j]['tree_dict'].items()):
                    if age*cnt <= MAP[i][j]['food']:
                        MAP[i][j]['food'] -= age*cnt
                        tmp_map[i][j][age + 1] = cnt

                        if (age + 1) % 5 == 0:
                            tmp_map[i][j][1] = tmp_map[i][j].get(1, 0) + cnt
                    else:
                        plus_cnt = MAP[i][j]['food'] // age
                        MAP[i][j]['food'] -= age*plus_cnt
                        tmp_map[i][j][age + 1] = plus_cnt
                        MAP[i][j]['tree_to_food'] += (age // 2)*(cnt - plus_cnt)

                        if (age + 1) % 5 == 0:
                            tmp_map[i][j][1] = tmp_map[i][j].get(1, 0) + plus_cnt

                    del MAP[i][j]['tree_dict'][age]
                
                for age, cnt in tmp_map[i][j].items():
                    MAP[i][j]['tree_dict'][age]
                # summer
                MAP[i][j]['food'] += MAP[i][j]['tree_to_food']
                MAP[i][j]['tree_to_food'] = 0

        # autumn
        for i in range(N):
            for j in range(N):
                MAP[i][j]['tree_dict'][1]