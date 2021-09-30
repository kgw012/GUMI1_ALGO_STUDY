# 프로그래머스 '소수 찾기'
# https://programmers.co.kr/learn/courses/30/lessons/42839

def dfs(numbers, visits, result_set, number):
    if number:
        int_num = int(number)
        
        flag = True
        for i in range(2, int_num):
            if i ** 2 > int_num:
                break
            if int_num % i == 0:
                flag = False
                break

        if flag and int_num > 1:
            result_set.add(int_num)
        
    for i, num in enumerate(numbers):
        if visits[i]:
            continue
        
        visits[i] = True
        dfs(numbers, visits, result_set, number + num)
        visits[i] = False
    
    return


def solution(numbers):    
    visits = [False for _ in range(len(numbers))]

    result_set = set()

    dfs(numbers, visits, result_set, '')
    answer = len(result_set)
    return answer


if __name__ == '__main__':
    numbers = '011'
    print(solution(numbers))