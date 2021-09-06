# 프로그래머스 '더 맵게'

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    cnt = 0
    while True:
        k1 = heapq.heappop(scoville)
        if k1 >= K:
            break
        
        if len(scoville) == 0:
            cnt = -1
            break

        cnt += 1
        k2 = heapq.heappop(scoville)
        heapq.heappush(scoville, k1 + k2 * 2)
    
    return cnt


if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    print(solution(scoville, K))