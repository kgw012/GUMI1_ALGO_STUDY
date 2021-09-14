# 프로그래머스 '이중우선순위 큐'

import heapq

def solution(operations):
    min_heap = []
    max_heap = []

    for op in operations:
        cmd, num = op.split()
        num = int(num)
        if cmd == 'I':
            heapq.heappush(min_heap, (num, num))
            heapq.heappush(max_heap, (-num, num))
        else:
            if len(min_heap) == 0:
                continue
            
            if num > 0:
                value = heapq.heappop(max_heap)
                min_heap.remove((-value[0], value[1]))
            else:
                value = heapq.heappop(min_heap)
                max_heap.remove((-value[0], value[1]))

    if len(min_heap) == 0:
        answer = [0, 0]
    else:
        answer = [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)[1]]

    return answer