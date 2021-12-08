# 백준 15686 '치킨 배달'
# https://www.acmicpc.net/problem/15686

def dfs(N, M, chickens, homes, visits, cnt, idx):
    if cnt >= M:
        total = 0
        for h_i, h_j in homes:
            min_d = 2*N
            for i, (c_i, c_j) in enumerate(chickens):
                if not visits[i]:
                    continue
                min_d = min(min_d, abs(h_i - c_i) + abs(h_j - c_j))
            
            total += min_d
        
        return total
    
    min_total = 2 * N * len(homes)
    for i in range(idx, len(chickens)):
        visits[i] = True
        min_total = min(min_total, dfs(N, M, chickens, homes, visits, cnt + 1, i + 1))
        visits[i] = False
    
    return min_total


if __name__ == '__main__':
    N, M = map(int, input().split())
    MAP = []
    for _ in range(N):
        MAP.append(list(map(int, input().split())))
    
    homes = []
    chickens = []
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 1:
                homes.append((i, j))
            if MAP[i][j] == 2:
                chickens.append((i, j))

    visits = [False] * len(chickens)
    answer = dfs(N, M, chickens, homes, visits, 0, 0)
    print(answer)
    