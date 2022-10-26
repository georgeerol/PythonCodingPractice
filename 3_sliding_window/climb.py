print("Hello")


# [10, 12, 18, 16, 19, 20, 18, 10]
# 8 = 18 - 10
# return 8

def biggest_climb(nums):
    profit = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            profit += max(nums[i] - nums[i - 1], 0)

    return profit

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    t1_cost, t2_cost = float('inf'), float('inf')
    t1_profit, t2_profit = 0, 0

    for price in prices:
        # the maximum profit if only one transaction is allowed
        t1_cost = min(t1_cost, price)
        t1_profit = max(t1_profit, price - t1_cost)
        # reinvest the gained profit in the second transaction
        t2_cost = min(t2_cost, price - t1_profit)
        t2_profit = max(t2_profit, price - t2_cost)

    return t2_profit


nums = [10, 12, 18, 16, 19, 20, 18, 10]
print(maxProfit(nums))
