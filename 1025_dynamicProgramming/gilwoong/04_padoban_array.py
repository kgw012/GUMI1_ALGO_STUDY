# 백준 9461 '파도반 수열'
# https://www.acmicpc.net/problem/9461

if __name__ == '__main__':
    dp = [0] * 101
    T = int(input())
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    dp[6] = 3
    dp[7] = 4
    dp[8] = 5
    idx = 9

    for t in range(T):
        N = int(input())

        while idx <= N:
            dp[idx] = dp[idx - 1] + dp[idx - 5]
            idx += 1
        
        print(dp[N])
