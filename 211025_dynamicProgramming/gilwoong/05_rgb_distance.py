# 백준 1149 'RGB거리'
# https://www.acmicpc.net/problem/1149

if __name__ == '__main__':
    N = int(input())
    home_list = []
    for _ in range(N):
        home_list.append(list(map(int, input().split())))
    
    r_dp = [0] * N
    g_dp = [0] * N
    b_dp = [0] * N

    r_dp[0] = home_list[0][0]
    g_dp[0] = home_list[0][1]
    b_dp[0] = home_list[0][2]

    for i in range(1, N):
        r_dp[i] = min(g_dp[i - 1], b_dp[i - 1]) + home_list[i][0]
        g_dp[i] = min(r_dp[i - 1], b_dp[i - 1]) + home_list[i][1]
        b_dp[i] = min(r_dp[i - 1], g_dp[i - 1]) + home_list[i][2]
        
    print(min(r_dp[N - 1], g_dp[N - 1], b_dp[N - 1]))
    