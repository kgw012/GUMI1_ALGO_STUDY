# 프로그래머스 '주식 가격'
# https://programmers.co.kr/learn/courses/30/lessons/42584

class Stock:
    def __init__(self, price, time):
        self.price = price
        self.time = time

def solution(prices):

    answer = [0 for _ in range(len(prices))]

    stack = []

    time = 0

    while time < len(prices):
        if len(stack) == 0:
            stack.append(Stock(prices[time], time))
            time += 1
            continue

        price = prices[time]
        top = stack[-1]

        if top.price > price:
            answer[top.time] = time - top.time
            stack.pop()
            continue
        
        stack.append(Stock(price, time))
        time += 1

    time -= 1

    while len(stack):
        pop = stack.pop()
        answer[pop.time] = time - pop.time

    return answer


if __name__=='__main__':
    prices = [1, 2, 3, 2, 3]
    answer = [4, 3, 1, 1, 0]
    my_answer = solution(prices)

    print('answer: {}, my_answer: {}'.format(answer, my_answer))