# 프로그래머스 'K번째 수'
# https://programmers.co.kr/learn/courses/30/lessons/42748

import heapq

def solution(array, commands):

    answer = []
    for cmd in commands:
        i, j, k = cmd

        heap = []

        for idx in range(i - 1, j):
            heapq.heappush(heap, array[idx])
        
        while True:
            num = heapq.heappop(heap)
            k -= 1

            if k == 0:
                answer.append(num)
                break
            
    return answer