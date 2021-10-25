# 백준 12765 '평범한 배낭'
# https://www.acmicpc.net/problem/12865

if __name__ == '__main__':
    N, K = map(int, input().split())
    lst = []
    for _ in range(N):
        lst.append(list(map(int, input().split())))
    
    dp = [[0] * (K + 1) for _ in range(N)]

    for i in range(N):
        w, v = lst[i]

        for j in range(1, K + 1):
            if j >= w:
                dp[i][j] = max(dp[i - 1][j - w] + v, dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    
    print(dp[N - 1][K])
    