def merge_sort(arr, st, end):
    if end - st < 2:
        return

    # divide
    mid = (st + end) // 2
    merge_sort(arr, st, mid)
    merge_sort(arr, mid, end)

    # conquer
    ret = []
    i, j = st, mid
    while i < mid and j < end:
        if arr[i] <= arr[j]:
            ret.append(arr[i])
            i += 1
        else:
            ret.append(arr[j])
            j += 1

    while i < mid:
        ret.append(arr[i])
        i += 1
    while j < end:
        ret.append(arr[j])
        j += 1

    for x in range(st, end):
        arr[x] = ret[x - st]


if __name__ == "__main__":
    test_arr = [3, 5, 8, 0, 100, 35, 2, 17, 5]
    merge_sort(test_arr, 0, len(test_arr))
    print(test_arr)
