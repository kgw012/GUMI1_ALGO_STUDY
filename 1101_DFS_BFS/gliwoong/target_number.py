# 프로그래머스 '타겟 넘버'
# https://programmers.co.kr/learn/courses/30/lessons/43165

def dfs(numbers, target, total, idx):
    if idx >= len(numbers):
        if total == target:
            return 1
        else:
            return 0
    
    answer = 0
    answer += dfs(numbers, target, total + numbers[idx], idx + 1)
    answer += dfs(numbers, target, total - numbers[idx], idx + 1)

    return answer


def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0)
    return answer