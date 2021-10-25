# 백준 11053 '가장 긴 증가하는 부분수열'
# https://www.acmicpc.net/problem/11053

if __name__ == '__main__':
    N = int(input())
    lst = list(map(int, input().split()))

    dp = [0] * N
    dp[0] = 1

    for i in range(1, N):
        max_cnt = 0

        for j in range(i):
            if lst[j] < lst[i]:
                max_cnt = max(max_cnt, dp[j])
        
        dp[i] = max_cnt + 1
    
    print(max(dp))
