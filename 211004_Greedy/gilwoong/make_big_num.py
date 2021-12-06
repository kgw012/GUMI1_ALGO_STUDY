def solution(number, k):
    stk = []
    for num in number:
        while stk and stk[-1] < num and k > 0:
            stk.pop()
            k -= 1
        
        stk.append(num)

    if k > 0:
        return ''.join(stk[:-k])
    else:
        return ''.join(stk)


if __name__ == '__main__':
    number = '1924'
    k = 2

    print(solution(number, k))