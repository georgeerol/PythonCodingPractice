def find_second_maximum(lst):
    # O(nLogn) time | O(1) space
    # SOrt and index - will not work if there's duplicate
    lst.sort()
    if len(lst) >= 2:
        return lst[-2]
    return None


def find_second_maximum(lst):
    # O(n) time | O(1) space
    # Traversing the list twice
    first_max = float('-inf')
    second_max = float('-inf')
    for item in lst:
        if item > first_max:
            first_max = item

    for item in lst:
        if item != first_max and item > second_max:
            second_max = item
    return second_max


if __name__ == "__main__":
    lst = [9, 2, 3, 6]
    print(find_second_maximum(lst))
