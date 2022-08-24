def find_product(lst):
    result = []
    # To store product of all previous values from currentIndex
    left = 1

    for i in range(len(lst)):
        current_product = 1
        for ele in lst[i + 1:]:
            current_product *= ele
        result.append(current_product * left)
        left *= lst[i]
    return result


def find_product_2(lst):
    # get product start from left
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left *= ele
    # get product starting from right
    right = 1
    for i in range(len(lst) - 1, -1, -1):
        product[i] *= right
        right *= lst[i]
    return product


if __name__ == '__main__':
    print(find_product([1, 2, 3, 4]))
    print(find_product_2([1, 2, 3, 4]))
