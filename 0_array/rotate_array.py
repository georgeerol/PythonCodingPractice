def rotate(nums, k):
    # (i + k) % length of array
    n = len(nums)
    a = [0] * n
    for i in range(n):
        a[(i + k) % n] = nums[i]
    return a


def rotate_2(nums, k):
    # Taking advantage of python's list indexing
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(rotate(nums, k))
    print(rotate_2(nums, k))
