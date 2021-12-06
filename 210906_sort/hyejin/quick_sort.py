def quick_sort(arr, start, end):
    print(f"(start, end) = {(start, end)} / arr[start:end] ", arr[start:end], end="")

    pivot, l, r = arr[start], start + 1, end - 1
    while True:
        while l <= r and arr[l] <= pivot:
            l += 1
        while l <= r and pivot <= arr[r]:
            r -= 1
        if l > r:
            break
        arr[l], arr[r] = arr[r], arr[l]

    arr[start], arr[r] = arr[r], pivot
    print(" >> ", arr[start:end])

    if start + 1 < r:
        quick_sort(arr, start, r)
    if r + 2 < end:
        quick_sort(arr, r + 1, end)


if __name__ == "__main__":
    test1 = [3, 5, 8, 0, 100, 35, 2, 17, 5]
    quick_sort(test1, 0, len(test1))
    print("소팅 결과 ", test1)

    test2 = [6, -8, 1, 12, 8, 3, 7, -7]
    quick_sort(test2, 0, len(test2))
    print("소팅 결과", test2)
