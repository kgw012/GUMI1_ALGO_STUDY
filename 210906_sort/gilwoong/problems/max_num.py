# 프로그래머스 '가장 큰 수'
# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    def key(number):
        value = str(number)
        cnt = 0
        while len(value) < 4:
            value += value[cnt]
            cnt += 1
        
        return (-int(value), number)
    
    numbers.sort(key=key)

    answer = ''

    for number in numbers:
        answer += str(number)

    if int(answer) == 0:
        return '0'
        
    return answer