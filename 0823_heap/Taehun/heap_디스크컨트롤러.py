import heapq

def solution(jobs):
    answer = 0
    heap = []
    task = []
    length = len(jobs)
    time = 0
    require_time = 0
    for y, x in jobs:
        heapq.heappush(heap, (y, x))

    while(1):
        # 만약 일과 heap에 둘다 썻다면 break
        if len(task) == 0 and len(heap) == 0:
            break
        # 만약 테스크는 종료했느느데 힙에 일이 남았으면
        # 테스크에 일을 추가하고 대기한 시간만큼 총 시간에 더해준다
        # 대기한 시간은 앞의 작업이 끝난시간에서 다음 작업의 요청시간의 차만큼 더해준다
        if len(task) == 0 and len(heap) > 0:
            temp = heapq.heappop(heap)
            before_time = time
            time += (temp[0] - before_time)
            heapq.heappush(task, (temp[1], temp[0]))
            continue

        elif len(task) > 0 and len(heap) > 0:
            complete_task = heapq.heappop(task)
            time += complete_task[0]
            require_time += (time - complete_task[1])
            # 힙이 있을 동안
            while(heap):
                # 현재 시간이 힙의 요청 시간보다 크거나 같은경우 추가한다 작업에, 단 작업량 순으로
                if time >= heap[0][0]:
                    temp = heapq.heappop(heap)
                    heapq.heappush(task, (temp[1], temp[0]))
                else:
                    break
        # 힙에서 다 추가한뒤 작업할 작업만 남으면
        elif len(task) > 0 and len(heap) == 0:
            while(task):
                complete_task = heapq.heappop(task)
                time += complete_task[0]
                require_time += (time - complete_task[1])


    answer = (require_time// length)





    return answer


jobs = [[0, 3], [1, 9], [2, 6]]

solution(jobs)

