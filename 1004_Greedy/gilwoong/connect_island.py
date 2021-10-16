# 프로그래머스 '섬 연결하기'
# https://programmers.co.kr/learn/courses/30/lessons/42861

def find(p_list, a):
    if p_list[a] == a:
        return a
    
    ret = find(p_list, p_list[a])
    p_list[a] = ret
    return ret
    

def union(p_list, a, b):
    pa = find(p_list, a)
    pb = find(p_list, b)

    if pa != pb:
        p_list[pa] = pb
    return
    

def solution(n, costs):
    p_list = [i for i in range(n)]
    costs.sort(key=lambda cost: cost[2])
    
    answer = 0
    for cost in costs:
        n1, n2, c = cost
        if find(p_list, n1) != find(p_list, n2):
            union(p_list, n1, n2)
            answer += c

    return answer