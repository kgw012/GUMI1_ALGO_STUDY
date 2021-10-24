import sys
input = sys.stdin.readline

N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            Map[i][j] += Map[i - 1][j]
        elif j == i:
            Map[i][j] += Map[i - 1][j - 1]
        else:
            Map[i][j] += max(Map[i - 1][j - 1], Map[i - 1][j])

print(max(Map[-1]))
