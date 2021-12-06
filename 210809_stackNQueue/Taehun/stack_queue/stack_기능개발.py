from collections import deque

def solution(progress, speeds):
    queue = deque()
    ans = []
    for i in range(len(progress)):
        time = 0
        while(1):
            if 100 <= progress[i] + (speeds[i] * time):
                break
            time += 1
        queue.append(time)
    max_time = queue.popleft()
    cnt = 1

    while (len(queue) > 0):
        time = queue.popleft()
        if max_time < time:
            max_time = time
            ans.append(cnt)
            cnt = 1

        else:
            cnt += 1

        if len((queue)) == 0:
            ans.append(cnt)

    print(ans)
    return ans




progress = [95, 90, 99, 99, 80, 99]
speeds = 	[1, 1, 1, 1, 1, 1]
answer = solution(progress, speeds)
