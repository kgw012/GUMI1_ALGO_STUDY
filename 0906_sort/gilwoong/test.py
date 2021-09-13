from mergesort import merge_sort
from quicksort import quick_sort

if __name__ == '__main__':
    lst1 = [9, 3, 1, 4, 2, 5, 8, 7, 6]
    lst2 = [9, 3, 1, 4, 2, 5, 8, 7, 6]

    merge_sort(lst1, 0, len(lst1))
    print(lst1)

    quick_sort(lst2, 0, len(lst2))
    print(lst2)