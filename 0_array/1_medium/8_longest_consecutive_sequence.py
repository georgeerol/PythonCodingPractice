def longest_consecutive(nums):
    '''
     1234    100  200
     convert to set
     100 ->
     200 ->
     1->2->3->4
    '''

    numSet = set(nums)
    longest = 0

    for n in nums:
        # check if its the start of a sequence
        if (n - 1) not in numSet:
            length = 0
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    print(longest_consecutive(nums))
