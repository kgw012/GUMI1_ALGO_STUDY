import heapq

def solution(jobs):
    answer = 0
    heap = []
    for y, x in jobs:
        heapq.heappush(heap, (y, x))
    work = []
    time = 0
    length = len(heap)
    task_time = 0
    total_time = 0
    while(1):

        if len(work) == 0 and len(heap) == 0:
            break

        # 작업공간이 비엇다면 work에 작업시간만큼 추가한다
        if len(work) == 0:
            task = heapq.heappop(heap)
            heapq.heappush(work, (task[1], task[0]))

        # 요청시간에 도달하게 되면 work에 시간을 추가한다
        if heap:
           if heap[0][0] == time:
                task = heapq.heappop(heap)
                heapq.heappush(work, (task[1], task[0]))
                continue

        if work:
            if work[0][0] == task_time:
                out_task = heapq.heappop(work)
                total_time += (time - out_task[1])
                task_time = 0
                continue
            else:
                task_time += 1
                time += 1



    answer = (int(total_time / length))


    return answer


jobs = [[0, 3], [1, 9], [2, 6]]

solution(jobs)

