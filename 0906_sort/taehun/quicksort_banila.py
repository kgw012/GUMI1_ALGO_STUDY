import random

def quicksort(lst, end, start=0): # 첫인자는 신경 안쓰도록 다만 내부 호출에서 end와 start 주의하자
    mutable_lst = lst

    if len(mutable_lst[start:end]) < 2:
        return

    pivot = mutable_lst[start]
    left_idx = start + 1
    right_idx = end
    while(left_idx <= right_idx): # 이부분때문에 에러남

        if mutable_lst[left_idx] >= pivot and mutable_lst[right_idx] < pivot:
            mutable_lst[left_idx], mutable_lst[right_idx] = mutable_lst[right_idx], mutable_lst[left_idx]
            left_idx += 1
            right_idx -= 1

        if mutable_lst[left_idx] < pivot:
            left_idx += 1

        if mutable_lst[right_idx] >= pivot:
            right_idx -= 1

    mutable_lst[start], mutable_lst[right_idx] = mutable_lst[right_idx], mutable_lst[start]
    quicksort(mutable_lst, right_idx, start)
    quicksort(mutable_lst, end, left_idx)

    return


for i in range(5):
    test = [i for i in range(50)]
    random.shuffle(test)
    print(f'원본 : {test}')
    quicksort(test, (len(test) - 1))
    print(f'정렬 후 : {test}')
    print('#' * 170)

