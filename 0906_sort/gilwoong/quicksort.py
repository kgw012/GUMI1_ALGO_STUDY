def quick_sort(lst, st, fn):
    if fn - st < 2:
        return
    
    pivot = st
    l = st + 1
    r = fn - 1

    while l < r:
        while lst[pivot] < lst[r]:
            r -= 1
        while lst[pivot] >= lst[l] and l < r:
            l += 1
        lst[l], lst[r] = lst[r], lst[l]

    lst[pivot], lst[r] = lst[r], lst[pivot]

    quick_sort(lst, st, r)
    quick_sort(lst, r, fn)

    return
