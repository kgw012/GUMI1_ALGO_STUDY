# 백준 1463 '1로 만들기'
# https://www.acmicpc.net/problem/1463

from collections import deque

def chcek_and_push(num, push_num):
    global visits, X, que

    if push_num > X:
        return False

    if visits[push_num]:
        return False

    visits[push_num] = visits[num] + 1
    que.append(push_num)

    if push_num == X:
        return True

    return False


if __name__ == '__main__':
    X = int(input())
    visits = [0] * 1000001
    
    que = deque()
    num = 1
    que.append(num)

    while que:
        num = que.popleft()
        
        flag = chcek_and_push(num, num + 1) or chcek_and_push(num, num * 2) or chcek_and_push(num, num * 3)

        if flag:
            break
    
    print(visits[X])
