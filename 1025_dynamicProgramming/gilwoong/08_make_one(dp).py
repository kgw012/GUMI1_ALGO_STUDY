# 백준 1463 '1로 만들기'
# https://www.acmicpc.net/problem/1463

def check_and_push(idx, num):
    global dp, X

    if idx >= len(dp):
        return
    
    dp[idx] = min(dp[idx], num)
    return


if __name__ == '__main__':
    X = int(input())
    dp = [1000000] * (X + 1)
    dp[1] = 0

    for i in range(1, X + 1):
        check_and_push(i + 1, dp[i] + 1)
        check_and_push(2 * i, dp[i] + 1)
        check_and_push(3 * i, dp[i] + 1)

    print(dp[X])
