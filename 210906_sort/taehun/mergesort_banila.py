from collections import deque
import random

def mergesort(lst):

    if len(lst) < 2:
        temp = lst
        return temp

    middle = len(lst) // 2
    left_lst = mergesort(lst[:middle])
    right_lst = mergesort(lst[middle:])
    return_lst = []
    left_idx = 0
    right_idx = 0

    while(1):
        if left_idx < len(left_lst) and right_idx < len(right_lst):
            left_value = left_lst[left_idx]
            right_value = right_lst[right_idx]
            if left_value <= right_value: # stable 정렬로 만들기 위해 =을 붙임
                return_lst.append(left_value)
                left_idx += 1
            else:
                return_lst.append(right_value)
                right_idx += 1

        elif left_idx >= len(left_lst) and right_idx < len(right_lst):
            right_value = right_lst[right_idx]
            return_lst.append(right_value)
            right_idx += 1

        elif left_idx < len(left_lst) and right_idx >= len(right_lst):
            left_value = left_lst[left_idx]
            return_lst.append(left_value)
            left_idx += 1

        elif left_idx >= len(left_lst) and right_idx >= len(right_lst):
            break

    return return_lst




#
a = [i for i in range(1, 10)]
for i in range(1, 6):
    random.shuffle(a)
    print(f'{i}번째 셔플 : {a}')
    ans = mergesort(a)
    print(f'정렬결과 : {ans}')
    block = '#' * 100
    print(block)



