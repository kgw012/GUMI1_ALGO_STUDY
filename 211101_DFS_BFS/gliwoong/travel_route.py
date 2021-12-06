# 프로그래머스 '여행경로'
# https://programmers.co.kr/learn/courses/30/lessons/43164

def dfs(tickets, visits, answer, cnt, airport):
    if cnt >= len(tickets):
        return True
    
    for i, ticket in enumerate(tickets):
        if visits[i]:
            continue

        if ticket[0] != airport:
            continue

        visits[i] = True
        answer.append(ticket[1])

        flag = dfs(tickets, visits, answer, cnt + 1, ticket[1])
        if flag:
            return True

        visits[i] = False
        answer.pop()

    return False


def solution(tickets):
    tickets.sort()
    visits = [False] * len(tickets)
    answer = ['ICN']

    for i, ticket in enumerate(tickets):
        if ticket[0] != 'ICN':
            continue

        visits[i] = True
        answer.append(ticket[1])

        flag = dfs(tickets, visits, answer, 1, ticket[1])
        if flag:
            break

        visits[i] = False
        answer.pop()

    return answer


if __name__ == '__main__':
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
    print(solution(tickets))
