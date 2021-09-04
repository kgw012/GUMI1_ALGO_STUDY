from collections import deque
def solution(prices):
    queue = deque(prices)
    answer = []

    index = 0
    while queue:
        cnt = -1
        now_num = queue.popleft()
        for i in range(index, len(prices)):
            if now_num > prices[i]:
                cnt += 1
                break
            cnt += 1
        index += 1
        answer.append(cnt)
    return answer


price = [1, 2, 3, 2, 3]
solution(price)