# 프로그래머스 '프린터'
# https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

class Print:
    def __init__(self, idx, priority):
        self.idx = idx
        self.priority = priority


def solution(priorities, location):
    print_que = deque([])
    priority_que = deque([])
    cnt_list = [0 for _ in range(10)]

    for idx, priority in enumerate(priorities):
        print_que.append(Print(idx, priority))
        cnt_list[priority] += 1
    
    for priority in range(9, 0, -1):
        while cnt_list[priority]:
            priority_que.append(priority)
            cnt_list[priority] -= 1
    
    answer = 0
    while True:
        print: Print = print_que.popleft()
        if print.priority == priority_que[0]:
            answer += 1
            priority_que.popleft()
            if print.idx == location:
                break
        else:
            print_que.append(print)

    return answer