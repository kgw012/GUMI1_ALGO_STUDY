# 프로그래머스 '디스크 컨트롤러'

import heapq

def solution(jobs):
    jobs.sort()

    heap = []

    time = 0
    idx = 0
    total = 0
    while heap or idx < len(jobs):
        while idx < len(jobs):
            job = jobs[idx]
            if job[0] <= time:
                heapq.heappush(heap, (job[1], job[0]))
                idx += 1
            else:
                break
        
        if not heap:
            time += 1
            continue
        
        pop_item = heapq.heappop(heap)
        total += (time - pop_item[1] + pop_item[0])
        time += pop_item[0]

    answer = total // len(jobs)
    return answer