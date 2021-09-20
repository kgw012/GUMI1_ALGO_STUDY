import heapq

def solution(array, commands):

    answer = []
    for cmd in commands:
        i, j, k = cmd

        heap = []

        for idx in range(i - 1, j):
            heapq.heappush(array[idx], array[idx])
        
        while True:
            num = heapq.heappop(array)
            k -= 1

            if k == 0:
                answer.append(num)
                break
            
    return answer