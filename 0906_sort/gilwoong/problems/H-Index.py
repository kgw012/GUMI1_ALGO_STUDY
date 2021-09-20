def solution(citations):
    n = len(citations)
    h = 0
    answer = 0

    while h <= n:
        cnt1 = 0
        cnt2 = 0
        for citation in citations:
            if h <= citation:
                cnt1 += 1
            else:
                cnt2 += 1
        
        if cnt1 >= h and cnt2 <= h:
            answer = h
        
        h += 1
        
    return answer