def solution(people, limit):
    people.sort()

    l = 0
    r = len(people) - 1
    answer = 0
    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1
            r -= 1
            answer += 1
        else:
            r -= 1
            answer += 1
            
    return answer