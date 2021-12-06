def solution(name):
    move = [min(ord(n) - ord('A'), ord('Z') - ord(n) + 1) for n in name]
    
    idx, answer = 0, 0
    while True:
        answer += move[idx]
        move[idx] = 0
        
        if not sum(move):
            return answer
        
        l = r = 1
        while not move[idx - l]:
            l += 1
        while not move[idx + r]:
            r += 1
        
        if l < r:
            answer += l
            idx -= l 
        else:
            answer += r
            idx += r
