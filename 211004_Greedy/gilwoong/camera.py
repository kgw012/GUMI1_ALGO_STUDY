# 프로그래머스 '단속카메라'
# https://programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    routes.sort(key=lambda route: route[1])

    i = 0
    camera = -30001
    answer = 0
    while i < len(routes):
        if routes[i][0] <= camera <= routes[i][1]:
            i += 1
            continue
        camera = routes[i][1]
        answer += 1
        i += 1
    
    return answer