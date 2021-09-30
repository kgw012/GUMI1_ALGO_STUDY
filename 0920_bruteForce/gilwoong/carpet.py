# 프로그래머스 '카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    y_divisors = []
    for i in range(1, yellow + 1):
        if i ** 2 > yellow:
            break
        if yellow % i == 0:
            y_divisors.append((yellow // i, i))
    
    answer = []
    for y_divisor in y_divisors:
        div1, div2 = y_divisor
        if 2 * (div1 + div2) + 4 == brown:
            answer = [div1 + 2, div2 + 2]

    return answer