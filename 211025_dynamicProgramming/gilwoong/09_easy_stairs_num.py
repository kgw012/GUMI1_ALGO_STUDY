# 백준 10844 '쉬운 계단 수'
# https://www.acmicpc.net/problem/10844

if __name__ == '__main__':
    N = int(input())

    dp = [[0] * 10 for _ in range(N + 1)]

    for i in range(1, 10):
        dp[1][i] = 1
    
    for i in range(2, N + 1):
        dp[i][0] = dp[i - 1][1]
        dp[i][9] = dp[i - 1][8]

        for j in range(1, 9):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 1000000000
    
    answer = 0
    for i in range(10):
        answer += dp[N][i]

    answer %= 1000000000
    print(answer)
