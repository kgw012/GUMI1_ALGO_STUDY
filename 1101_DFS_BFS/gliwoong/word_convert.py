# 프로그래머스 '단어 변환'
# https://programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def solution(begin, target, words):
    n = len(begin)

    que = deque()
    level = 0
    que.append((begin, level))

    flag = False
    while que:
        word, level = que.popleft()
        if word == target:
            flag = True
            break

        for i, n_word in enumerate(words):
            cnt = 0
            for j in range(n):
                if cnt > 1:
                    break
                if word[j] != n_word[j]:
                    cnt += 1
            
            if cnt == 1:
                que.append((n_word, level + 1))
                words.pop(i)
    
    if flag:
        answer = level
    else:
        answer = 0

    return answer
