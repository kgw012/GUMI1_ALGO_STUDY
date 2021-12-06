# 백준 2565 '전깃줄'
# https://www.acmicpc.net/problem/2565

if __name__ == '__main__':
    n = int(input())
    wires = []
    for _ in range(n):
        wires.append(list(map(int, input().split())))
    
    wires.sort()

    dp = [0] * n
    dp[0] = 1

    for i in range(1, n):
        max_cnt = 0
        for j in range(i):
            if wires[j][1] < wires[i][1]:
                max_cnt = max(max_cnt, dp[j])
        dp[i] = max_cnt + 1
    
    answer = n - max(dp)
    print(answer)
