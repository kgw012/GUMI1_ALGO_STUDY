# 프로그래머스 '순위'
# https://programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    adj = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for winner, loser in results:
        adj[winner][loser] = 1
        adj[loser][winner] = -1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if adj[i][j] == 0:
                continue
            
            for k in range(1, n + 1):
                if adj[i][j] == 1 and adj[j][k] == 1:
                    adj[i][k] = 1
                    adj[k][i] = -1
                elif adj[j][i] == 1 and adj[k][j] == 1:
                    adj[k][i] = 1
                    adj[i][k] = -1
        
    answer = 0
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if adj[i][j] != 0:
                cnt += 1
        
        if cnt == n - 1:
            answer += 1

    print(adj)
    return answer