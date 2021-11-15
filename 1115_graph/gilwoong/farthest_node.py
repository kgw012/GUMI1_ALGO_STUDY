# 프로그래머스 '가장 먼 노드'
# https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque

def solution(n, edge):
    node_dict = dict()
    for n1, n2 in edge:
        if n1 not in node_dict:
            node_dict[n1] = list()
        if n2 not in node_dict:
            node_dict[n2] = list()
        
        node_dict[n1].append(n2)
        node_dict[n2].append(n1)
    
    visits = [False] * (n + 1)

    que = deque()
    que.append((1, 0))
    visits[1] = True

    answer = 0
    max_level = 0
    while que:
        node, level = que.popleft()
        if max_level < level:
            max_level = level
            answer = 1
        else:
            answer += 1

        for n_node in node_dict[node]:
            if visits[n_node]:
                continue
            
            visits[n_node] = True
            que.append((n_node, level + 1))

    return answer