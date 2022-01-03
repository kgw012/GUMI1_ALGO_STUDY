# 백준 20057 '마법사 상어와 토네이도'
# https://www.acmicpc.net/problem/20057

from sys import stdin

input = stdin.readline

di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

def point_sand(point, sand, d):
    i, j = point
    res = []
    cnt = 0

    # 5%
    ni = i + 2 * di[d]
    nj = j + 2 * dj[d]
    ns = int(sand * 0.05)
    res.append(((ni, nj), ns))
    cnt += ns

    for k in range(2):
        # 10%
        ni = i + di[d] + di[(d + 1 + 2*k) % 4]
        nj = j + dj[d] + dj[(d + 1 + 2*k) % 4]
        ns = int(sand * 0.1)
        res.append(((ni, nj), ns))
        cnt += ns

        # 7%
        ni = i + di[(d + 1 + 2*k) % 4]
        nj = j + dj[(d + 1 + 2*k) % 4]
        ns = int(sand * 0.07)
        res.append(((ni, nj), ns))
        cnt += ns

        # 2%
        ni = i + 2 * di[(d + 1 + 2*k) % 4]
        nj = j + 2 * dj[(d + 1 + 2*k) % 4]
        ns = int(sand * 0.02)
        res.append(((ni, nj), ns))
        cnt += ns
        
        # 1%
        ni = i - di[d] + di[(d + 1 + 2*k) % 4]
        nj = j - dj[d] + dj[(d + 1 + 2*k) % 4]
        ns = int(sand * 0.01)
        res.append(((ni, nj), ns))
        cnt += ns
    
    # alpha
    ni = i + di[d]
    nj = j + dj[d]
    ns = sand - cnt
    res.append(((ni, nj), ns))

    return res


if __name__ == '__main__':
    N = int(input())
    MAP = []
    for _ in range(N):
        MAP.append(list(map(int, input().split())))
    
    answer = 0

    i, j = N // 2, N // 2
    cnt = 0
    d = 0
    while cnt // 2 < N - 1:
        for _ in range(cnt // 2 + 1):
            ni = i + di[d]
            nj = j + dj[d]
            sand_list = point_sand((ni, nj), MAP[ni][nj], d)
            for point, sand in sand_list:
                nni, nnj = point
                if (0 <= nni < N and 0 <= nnj < N):
                    MAP[nni][nnj] += sand
                else:
                    answer += sand

            i = ni
            j = nj

        cnt += 1
        d = (d + 1) % 4
    
    for _ in range(N - 1):
        ni = i + di[d]
        nj = j + dj[d]
        sand_list = point_sand((ni, nj), MAP[ni][nj], d)
        for point, sand in sand_list:
            nni, nnj = point
            if (0 <= nni < N and 0 <= nnj < N):
                MAP[nni][nnj] += sand
            else:
                answer += sand

        i = ni
        j = nj
    
    print(answer)
    