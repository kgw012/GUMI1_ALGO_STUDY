# 백준 1904 '01타일'
# https://www.acmicpc.net/problem/1904

if __name__ == '__main__':
    N = int(input())

    dp = [0] * (N + 1)

    dp[1] = 1

    dp[2] = 2

    for i in range(3, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
    
    print(dp[N])
    