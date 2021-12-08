# 백준 14891 '톱니바퀴'
# https://www.acmicpc.net/problem/14891

def rotate(gears:list, ptrs:list, visits:list, k:int, d:int):
    visits[k] = True
    
    if k + 1 < 4 and not visits[k + 1]:
        ns1 = gears[k][(ptrs[k] + 2) % 8]
        ns2 = gears[k + 1][(ptrs[k + 1] + 6) % 8]
        if ns1 != ns2:
            rotate(gears, ptrs, visits, k + 1, -d)
    
    if k - 1 >= 0 and not visits[k - 1]:
        ns1 = gears[k - 1][(ptrs[k - 1] + 2) % 8]
        ns2 = gears[k][(ptrs[k] + 6) % 8]
        if ns1 != ns2:
            rotate(gears, ptrs, visits, k - 1, -d)

    if d == 1:
        ptrs[k] = (ptrs[k] + 7) % 8
    else:
        ptrs[k] = (ptrs[k] + 1) % 8

    return


if __name__ == '__main__':
    gears = []
    for i in range(4):
        gears.append(list(map(int, list(input()))))
    
    ptrs = [0, 0, 0, 0]
    
    K = int(input())
    for _ in range(K):
        k, d = map(int, input().split())
        visits = [False] * 4
        rotate(gears, ptrs, visits, k - 1, d)

    score = 0
    for i in range(4):
        if gears[i][ptrs[i]] == 1:
            score += 2**i
    
    print(score)
