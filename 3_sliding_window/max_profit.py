# Time: O(n)
# mem: O(n)
def max_profit(prices):
    result = 0
    left_pointer = 0
    for right_pointer in range(1, len(prices)):
        if prices[right_pointer] < prices[left_pointer]:
            left_pointer = right_pointer
        result = max(result, prices[right_pointer] - prices[left_pointer])
    return result


def max_profit_2(prices):
    l, r = 0, 1  # left = buy, right =sell
    max_price = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_price = max(max_price, profit)
        else:
            l = r
        r += 1
    return max_price


if __name__ == '__main__':
    p = [7, 1, 5, 3, 6, 4]
    print(max_profit(p))
    print(max_profit_2(p))
