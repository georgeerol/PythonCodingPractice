def product_except_self(nums):
    """
    input: [1,2,3,4]
    prefix: [1,2,6,24]
    postfix: [24,24,12,4]
    output: [24,12,8,9]
    """

    res = [1] * (len(nums))

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(product_except_self(nums))
