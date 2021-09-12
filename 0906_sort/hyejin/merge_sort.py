def merge_sort(arr):
    if len(arr) == 1:
        return arr

    # divide
    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    # conquer
    ret = []
    i, j = 0, 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            ret.append(left_arr[i])
            i += 1
        else:
            ret.append(right_arr[j])
            j += 1

    if i < len(left_arr):
        ret += left_arr[i:]
    else:
        ret += right_arr[j:]
    return ret


if __name__ == "__main__":
    test_arr = [3, 5, 8, 0, 100, 35, 2, 17, 5]
    sorted_arr = merge_sort(test_arr)
    print(sorted_arr)
