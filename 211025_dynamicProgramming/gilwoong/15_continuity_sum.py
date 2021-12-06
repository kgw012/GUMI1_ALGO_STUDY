# 백준 1912 '연속합'
# https://www.acmicpc.net/problem/1912

if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))

    dp = [0] * n
    dp[0] = lst[0]
    for i in range(1, n):
        dp[i] = max(0, dp[i - 1] + lst[i])
    
    answer = max(dp)
    if answer <= 0:
        answer = max(lst)
    
    print(answer)
    