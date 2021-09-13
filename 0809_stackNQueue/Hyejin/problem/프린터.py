def solution(priorities, location):
    arr = [[p, idx] for idx, p in enumerate(priorities)]

    answer = 0
    while arr:
        tmp = arr.pop(0)
        flag = False
        for a in arr:
            if a[0] > tmp[0]:
                flag = True
                break
        if flag:
            arr.append(tmp)
        else:
            answer += 1
            if tmp[1] == location:
                return answer
