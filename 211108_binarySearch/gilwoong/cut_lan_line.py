# 백준 1654 '랜선 자르기'
# https://www.acmicpc.net/problem/1654

from sys import stdin

if __name__ == '__main__':
    K, N = map(int, stdin.readline().split())

    lines = []
    max_line = 0
    for _ in range(K):
        line = int(stdin.readline())
        max_line = max(max_line, line)
        lines.append(line)
    
    l = 0
    r = max_line + 1

    while l < r:
        md = (l + r) // 2

        cnt = 0
        for line in lines:
            cnt += (line // md)
        
        if cnt >= N:
            l = md + 1
        else:
            r = md
    
    print(l - 1)
