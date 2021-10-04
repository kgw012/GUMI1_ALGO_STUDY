def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    answer = n - len(lost)
    
    reserve_std = [False for _ in range(n + 1)]
    
    for reserve_idx in reserve:
        reserve_std[reserve_idx] = True
        
    for lost_idx in range(len(lost)):
        if reserve_std[lost[lost_idx]]:
            reserve_std[lost[lost_idx]] = False
            answer += 1
            lost[lost_idx] = -1
            continue
            
    for lost_std in lost:
        if lost_std < 0:
            continue
            
        if lost_std - 1 >= 0 and reserve_std[lost_std - 1]:
            reserve_std[lost_std - 1] = False
            answer += 1
            continue
        
        if lost_std + 1 <= n and reserve_std[lost_std + 1]:
            reserve_std[lost_std + 1] = False
            answer += 1
            continue
        
    return answer