# 백준 9251 'LCS' (최장 공통 부분 수열)
# https://www.acmicpc.net/problem/9251

if __name__ == '__main__':
    str1 = input()
    str2 = input()

    n1 = len(str1)
    n2 = len(str2)

    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

    for i in range(n1):
        for j in range(n2):
            if str1[i] == str2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    
    print(dp[n1][n2])
