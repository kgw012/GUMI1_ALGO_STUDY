# 백준 15685 '드래곤 커브'
# https://www.acmicpc.net/problem/15685

N = int(input())
curves = []
for _ in range(N):
    curves.append(list(map(int, input().split())))

MAP = [[False for _ in range(101)] for _ in range(101)]

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

for curve in curves:
    j, i, d, g = curve

    d_list = [d]

    for _ in range(g):
        d_len = len(d_list)
        for idx in range(d_len - 1, -1, -1):
            d_list.append((d_list[idx] + 1) % 4)

    for d in d_list:
        MAP[i][j] = True
        ni = i + di[d]
        nj = j + dj[d]
        MAP[ni][nj] = True

        i, j = ni, nj

cnt = 0

for i in range(100):
    for j in range(100):
        if MAP[i][j] and MAP[i + 1][j] and MAP[i][j + 1] and MAP[i + 1][j + 1]:
            cnt += 1

print(cnt)
