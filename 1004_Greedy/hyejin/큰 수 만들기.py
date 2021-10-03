from collections import deque


def solution(number, k):
    number = deque(number)
    stack = [number.popleft()]

    while number:
        n = number.popleft()

        while stack and k and stack[-1] < n:
            stack.pop()
            k -= 1

        stack.append(n)

    while k:
        stack.pop()
        k -= 1

    return ''.join(stack)
