# 프로그래머스 '다리를 지나는 트럭'
# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0

    i = 0
    w = 0
    que = deque([0 for _ in range(bridge_length)])

    while True:
        if i == len(truck_weights):
            time += bridge_length
            break
        
        w -= que.popleft()

        if w + truck_weights[i] <= weight:
            w += truck_weights[i]
            que.append(truck_weights[i])
            i += 1
        
        else:
            que.append(0)
        
        time += 1

    return time


if __name__=='__main__':
    test_cases = [
        {
            'bridge_length': 2,
            'weight': 10,
            'truck_weights': [7,4,5,6],
            'answer': 8
        }
    ]

    for test_case in test_cases:
        bridge_length = test_case['bridge_length']
        weight = test_case['weight']
        truck_weights = test_case['truck_weights']
        answer = test_case['answer']
        my_answer = solution(bridge_length, weight, truck_weights)

        print('answer: {}, my_answer: {}'.format(answer, my_answer))
    