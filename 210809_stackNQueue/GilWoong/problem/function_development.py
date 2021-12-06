# 프로그래머스 '기능개발'
# https://programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque
import math

def solution(progresses, speeds):

    p_que = deque(progresses)
    s_que = deque(speeds)

    
    time = 0
    answer = []

    while len(p_que):
        time = math.ceil((100 - p_que[0]) / s_que[0])
        
        cnt = 0
        while len(p_que)  and  100 - p_que[0] <= s_que[0] * time:
            p_que.popleft()
            s_que.popleft()
            cnt += 1
        
        answer.append(cnt)
    return answer


if __name__=='__main__':
    
    test_cases = [
        {
            'progresses': [93, 30, 55],
            'speeds': [1, 30, 5],
            'answer': [2, 1] 
        },
        {
            'progresses': [95, 90, 99, 99, 80, 99],
            'speeds': [1, 1, 1, 1, 1, 1],
            'answer': [1, 3, 2]
        }
    ]
    
    for test_case in test_cases:
        progresses = test_case['progresses']
        speeds = test_case['speeds']
        answer = test_case['answer']
        my_answer = solution(progresses, speeds)

        print(f'answer: {answer}, my_answer: {my_answer}')