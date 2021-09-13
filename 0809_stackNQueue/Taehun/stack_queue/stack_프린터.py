from collections import deque

def solution(priorities, location):

    print_queue = deque(priorities)
    locate_ls = [i for i in range(len(priorities))]
    locate_queue = deque(locate_ls)
    cnt = 0
    while print_queue:
        a = print_queue.popleft()
        b = locate_queue.popleft()
        for i in print_queue:
            if i > a:
                print_queue.append(a)
                locate_queue.append(b)
                break
        else:
            cnt += 1
            if b == location:
                return cnt





