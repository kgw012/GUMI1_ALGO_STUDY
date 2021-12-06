# 백준 1003 '피보나치 함수'
# https://www.acmicpc.net/problem/1003

if __name__ == '__main__':
    dp0 = [0] * 41
    dp1 = [0] * 41

    dp0[0] = 1
    dp1[0] = 0
    dp0[1] = 0
    dp1[1] = 1

    idx = 2

    T = int(input())

    for _ in range(T):
        N = int(input())

        while(idx <= N):
            dp0[idx] = dp0[idx - 1] + dp0[idx - 2]
            dp1[idx] = dp1[idx - 1] + dp1[idx - 2]
            idx += 1
        
        print(f'{dp0[N]} {dp1[N]}')
    