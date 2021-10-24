# 백준 2579 '계단 오르기'
# https://www.acmicpc.net/problem/2579

if __name__ == '__main__':
    n = int(input())
    stairs = []
    for _ in range(n):
        stairs.append(int(input()))
    
    dp1 = [0] * n
    dp2 = [0] * n

    dp1[0] = stairs[0]
    dp2[0] = stairs[0]
    
    if n >= 2:
        dp1[1] = stairs[1]
        dp2[1] = stairs[0] + stairs[1]
    
    for i in range(2, n):
        dp1[i] = max(dp1[i - 2], dp2[i - 2]) + stairs[i]
        dp2[i] = dp1[i - 1] + stairs[i]
    
    answer = max(dp1[n - 1], dp2[n - 1])
    print(answer)
