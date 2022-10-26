from typing import List


def find_sum(lst, k):
    # T: O(^2)
    # Brute Force
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] + lst[j] is k and i is not j:
                return [lst[i], lst[j]]


def binary_search(a, item):
    first = 0
    last = len(a) - 1
    found = False
    index = -1
    while first <= last and not found:
        mid = (first + last) // 2
        if a[mid] == item:
            index = mid
            found = True
        else:
            if item < a[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if found:
        return index
    else:
        return -1


def find_sum_2(lst, k):
    lst.sort()
    for j in range(len(lst)):
        # find the difference in list through binary search
        # return the only if we find an index
        index = binary_search(lst, k - lst[j])
        if index not in [-1, j]:
            return [lst[j], k - lst[j]]


def find_sum_3(lst, k):
    # O(n) time | O(n) space
    nums = {}
    for num in lst:
        value = k - num
        if value in nums:
            return [value, num]
        else:
            nums[num] = True
    return []


def find_sum_4(lst: List, k: int):
    # O(nlog(n) | O(1) space
    lst.sort()  # O(nlog(n)
    left = 0
    right = len(lst) - 1
    while left < right:
        current_sum = lst[left] + lst[right]
        if current_sum == k:
            return [lst[left], lst[right]]
        elif current_sum < k:
            left += 1
        elif current_sum > k:
            right -= 1
    return []


def find_sum_5(lst: List, k: int):
    # O(n) | O(1) space
    found_values = set()
    for ele in lst:
        if k - ele in found_values:
            return [k - ele, ele]
        found_values.add(ele)
    return []


if __name__ == "__main__":
    lst = [1, 2, 3, 5]
    k = 5
    print(find_sum(lst, k))
    print(find_sum_2(lst, k))
    print(find_sum_3(lst, k))
    print(find_sum_4(lst, k))
    print(find_sum_5(lst, k))
