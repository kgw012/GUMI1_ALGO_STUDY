# 프로그래머스 '방의 개수'
# https://programmers.co.kr/learn/courses/30/lessons/49190

def solution(arrows):
    di = [-1, -1, 0, 1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]

    i, j = 0, 0
    line_dict = dict()
    line_dict[(i, j)] = set()

    answer = 0
    for d in arrows:
        ni = i + di[d]
        nj = j + dj[d]

        if (ni, nj) in line_dict[(i, j)]:
            i = ni
            j = nj
            continue

        if (ni, nj) in line_dict.keys():
            answer += 1
            line_dict[(ni, nj)].add((i, j))
            line_dict[(i, j)].add((ni, nj))
        else:
            line_dict[(ni, nj)] = set()
            line_dict[(ni, nj)].add((i, j))
            line_dict[(i, j)].add((ni, nj))
        
        if d % 2 == 1:
            d2 = (d + 7) % 8
            ni2 = i + di[d2]
            nj2 = j + dj[d2]

            d3 = (d + 2) % 8
            ni3 = ni2 + di[d3]
            nj3 = nj2 + dj[d3]

            if (ni2, nj2) in line_dict.keys():
                if (ni3, nj3) in line_dict[(ni2, nj2)]:
                    answer += 1
        
        i = ni
        j = nj
        
    return answer