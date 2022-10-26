import math


def maximum_difference(nums):
    diff = -1  # in case there are no available maxim difference
    minimum = math.inf
    for i, n in enumerate(nums):
        if i > 0 and n > minimum:
            diff = max(diff, n - minimum)  # compare and save bigger value
        minimum = min(minimum, n)  # save minimum
    return diff


if __name__ == '__main__':
    print(maximum_difference([9, 4, 3, 2]))
    print(maximum_difference([1, 5, 2, 10]))
