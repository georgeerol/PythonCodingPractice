def two_sum(nums, target):
    hash_map = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hash_map:
            return [i, hash_map[diff]]
        else:
            hash_map[nums[i]] = i
    return []


def two_sum_2(nums, target):
    hash_map = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hash_map:
            return [i, hash_map[diff]]
        hash_map[n] = i
    return []


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    target = 5
    print(two_sum_2(arr, target))
