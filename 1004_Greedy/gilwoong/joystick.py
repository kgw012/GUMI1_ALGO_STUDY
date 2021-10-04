def solution(name):
    n = len(name)
    string = ['A' for _ in range(n)]

    answer = ord(name[0]) - ord('A')
    if answer > 13:
        answer = 26 - answer
    
    cnt = 0

    for c in name:
        if c == 'A':
            cnt += 1

    idx = 0
    while cnt < n:
        r = (idx + 1) % n
        r_d = 1
        while name[r] != string[r]:
            print(r)
            if r == idx:
                break
            r = (r + 1) % n
            r_d += 1
        
        l = (idx - 1 + n) % n
        l_d = 1
        while name[l] != string[l]:
            print(l)
            if l == idx:
                break
            l = (l - 1 + n) % n
            l_d += 1
        

        if r_d < l_d:
            idx = r
            d = r_d
        else:
            idx = l
            d = l_d
        
        char_d = ord(name[idx]) - ord('A')
        if char_d > 13:
            char_d = 26 - char_d
        
        answer += (d + char_d)
        cnt += 1
        string[idx] = name[idx]
        print(idx, d, char_d)

    return answer