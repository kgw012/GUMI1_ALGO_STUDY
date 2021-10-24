# 백준 1932 '정수 삼각형'
# https://www.acmicpc.net/problem/1932

if __name__ == '__main__':
    n = int(input())
    triangle = []
    for _ in range(n):
        triangle.append(list(map(int, input().split())))
    
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = triangle[0][0]

    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + triangle[i][0]
        dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
    
    for i in range(2, n):
        for j in range(1, i):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
    
    answer = max(dp[n - 1])
    print(answer)
