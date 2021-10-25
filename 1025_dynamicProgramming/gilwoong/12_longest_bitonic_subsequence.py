# 백준 11054 '가장 긴 바이토닉 부분 수열'
# https://www.acmicpc.net/problem/11054

if __name__ == '__main__':
    N = int(input())
    lst = list(map(int, input().split()))

    dp1 = [0] * N
    dp2 = [0] * N

    dp1[0] = 1
    dp2[N - 1] = 1

    for i in range(1, N):
        max_cnt1 = 0
        max_cnt2 = 0
        for j in range(i):
            if lst[j] < lst[i]:
                max_cnt1 = max(max_cnt1, dp1[j])
            if lst[N - j - 1] < lst[N - i - 1]:
                max_cnt2 = max(max_cnt2, dp2[N - j - 1])
        
        dp1[i] = max_cnt1 + 1
        dp2[N - i  -1] = max_cnt2 + 1
    
    answer = 0
    for i in range(N):
        answer = max(answer, dp1[i] + dp2[i] - 1)
        
    print(answer)
