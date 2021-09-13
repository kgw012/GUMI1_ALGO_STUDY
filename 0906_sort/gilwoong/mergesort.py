def merge_sort(lst, st, fn):
    if fn - st < 2:
        return

    md = (st + fn) // 2
    merge_sort(lst, st, md)
    merge_sort(lst, md, fn)

    l = st
    r = md

    tmp_lst = []
    while True:
        if (l >= md) or (r >= fn):
            break

        if lst[l] <= lst[r]:
            tmp_lst.append(lst[l])
            l += 1
        else:
            tmp_lst.append(lst[r])
            r += 1
    
    while l < md:
        tmp_lst.append(lst[l])
        l += 1
    
    while r < fn:
        tmp_lst.append(lst[r])
        r += 1
    
    for i in range(st, fn):
        lst[i] = tmp_lst[i - st]
    
    return

