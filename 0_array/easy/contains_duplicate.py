def contains_duplicate(nums):
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


if __name__ == '__main__':
    duplicate_nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(contains_duplicate(duplicate_nums))

