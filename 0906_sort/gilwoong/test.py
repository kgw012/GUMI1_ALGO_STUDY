import random

from mergesort import merge_sort
from quicksort import quick_sort

if __name__ == '__main__':
    size = 30
    lst1 = [i for i in range(size)]
    lst2 = [i for i in range(size)]
    random.shuffle(lst1)
    random.shuffle(lst2)

    # merge_sort(lst1, 0, len(lst1))
    # print(lst1)

    quick_sort(lst2, 0, len(lst2))
    print(lst2)