def merge_lists(lst1, lst2):
    """
     Traverse Both lists and insert smaller value from arr1 or arr2
     into result list and then increment that lists index.
     If a list is completely traversed, while other one is left then just
     copy all the remaining elements into result list

     This algorithm is O(n+m)
    O(n+m) where n and mm are the lengths of the lists. This is because both lists are iterated over at least once.
    """
    index_arr1 = 0
    index_arr2 = 0
    index_result = 0

    result = [i for i in range(len(lst1) + len(lst2))]

    while (index_arr1 < len(lst1)) and (index_arr2 < len(lst2)):
        if lst1[index_arr1] < lst2[index_arr2]:
            result[index_result] = lst1[index_arr1]
            index_arr1 += 1
        else:
            result[index_result] = lst2[index_arr2]
            index_arr2 += 1
        index_result += 1
    while index_arr1 < len(lst1):
        result[index_result] = lst1[index_arr1]
        index_result += 1
        index_arr1 += 1
    while index_arr2 < len(lst2):
        result[index_result] = lst2[index_arr2]
        index_result += 1
        index_arr2 += 1
    return result


def merge_lists2(lst1, lst2):
    index1 = 0
    index2 = 0

    while index1 < len(lst1) and index2 < len(lst2):
        if lst1[index1] > lst2[index2]:
            # insert list2's current index to list1
            lst1.insert(index1, lst2[index2])
            index1 += 1
            index2 += 1
        index1 += 1
    if index2 < len(lst2):
        lst1.extend(lst2[index2:])
    return lst1


if __name__ == '__main__':
    print(merge_lists([4, 5, 6], [-2, -1, 0, 7]))
    print(merge_lists2([4, 5, 6], [-2, -1, 0, 7]))
