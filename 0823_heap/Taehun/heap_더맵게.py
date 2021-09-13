import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    while(1):
        num1 = heapq.heappop(heap)
        if num1 >= K:
            break
        if heap:
            num2 = heapq.heappop(heap)
            heapq.heappush(heap, num1 + (num2 * 2))
            answer += 1
        else:
            answer = -1
            return answer

    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
solution(scoville, K)
