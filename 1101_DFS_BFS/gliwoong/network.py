# 프로그래머스 '네트워크'
# https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3

def find(p_list, a):
    if p_list[a] == a:
        return a
    
    res = find(p_list, p_list[a])
    p_list[a] = res
    return res


def union(p_list, a, b):
    pa = find(p_list, a)
    pb = find(p_list, b)

    if pa != pb:
        p_list[pa] = pb
    
    return


def solution(n, computers):
    p_list = [i for i in range(n)]

    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                union(p_list, i, j)
    
    for i in range(n):
        find(p_list, i)

    answer = len(set(p_list))

    return answer
