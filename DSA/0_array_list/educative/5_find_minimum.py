def find_minimum(lst):
    if len(lst) <= 0:
        return None
    lst.sort()
    return lst[0]


def find_minimum_2(lst):
    if len(lst) <= 0:
        return None
    merge_sort(lst)
    return lst[0]


def merge_sort(lst):
    if len(lst) <= 1:
        return

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    # recursive call on each half
    merge_sort(left)
    merge_sort(right)

    # Two iterators for traversing the two halves
    i = 0
    j = 0

    # Iterator for the main list
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[i]
            j += 1
        k += 1
    # For all the remaining values
    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__':
    print(find_minimum_2([9, 2, 3, 6]))
