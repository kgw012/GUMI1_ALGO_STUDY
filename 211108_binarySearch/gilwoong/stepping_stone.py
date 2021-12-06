# 프로그래머스 '징검다리'
# https://programmers.co.kr/learn/courses/30/lessons/43236

def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    l = 0
    r = distance + 1

    answer = 10e9
    while l < r:
        md = (l + r) // 2

        min_distance = 10e9
        idx = 0
        cnt = 0

        for rock in rocks:
            distance = rock - idx
            if distance >= md:
                idx = rock
                min_distance = min(min_distance, distance)
            else:
                cnt += 1

        if cnt <= n:
            l = md + 1
            answer = min_distance
        else:
            r = md
    
    return answer