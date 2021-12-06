# 백준 2156 '포도주 시식'
# https://www.acmicpc.net/problem/2156

if __name__ == '__main__':
    n = int(input())
    wines = []
    for _ in range(n):
        wines.append(int(input()))
    
    if n == 1:
        answer = wines[0]
        answer = wines[0]

    elif n == 2:
        answer = wines[0] + wines[1]
    
    else:
        dp0 = [0] * n
        dp1 = [0] * n
        dp2 = [0] * n

        dp0[0] = 0
        dp1[0] = wines[0]
        dp2[0] = 0

        dp0[1] = wines[0]
        dp1[1] = wines[1]
        dp2[1] = wines[0] + wines[1]
    
        for i in range(2, n):
            dp0[i] = max(dp0[i - 1], dp1[i - 1], dp2[i - 1])
            dp1[i] = dp0[i - 1] + wines[i]
            dp2[i] = dp1[i - 1] + wines[i]
        
        answer = max(dp0[n - 1], dp1[n - 1], dp2[n - 1])
    
    print(answer)
    