# 백준 9184 '신나는 함수 실행'
# https://www.acmicpc.net/problem/9184

def w(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    global dp
    if dp[a][b][c] is not None:
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    
    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]


if __name__ == '__main__':
    answer = ''
    dp = [[[None for _ in range(21)] for _ in range(21)] for _ in range(21)]

    while True:
        a, b, c = map(int, input().split())

        if a == -1 and b == -1 and c == -1:
            break
        
        result = w(a, b, c)
        answer += f'w({a}, {b}, {c}) = {result}\n'
    
    print(answer, end='')
    