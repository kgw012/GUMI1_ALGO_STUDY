# 프로그래머스 '모의고사'
# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    solves = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    students = []

    max_point = 0
    for std_num, solve in enumerate(solves, start=1):
        point = 0
        idx = 0
        while idx < len(answers):
            if solve[idx % len(solve)] == answers[idx]:
                point += 1
            idx += 1
        
        if point > max_point:
            max_point = point
        students.append((-point, std_num))

    students.sort()
    answer = []
    for std in students:
        if max_point != -std[0]:
            break
        answer.append(std[1])

    return answer