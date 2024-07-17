from typing import List


def maxProfit(prices: List[int]) -> int:
    """
    Keep track of the minimum price to buy stock and calculate and store profit for each day.
    Time complexity: 0(n), one itteration is the most expensive operation.
    Space Complexity: O(1), store only constant.
    """
    days = len(prices)
    max_profit = 0
    if days == 1:
        return 0
    buy_price = prices[0]
    for index in range(1, days):
        if buy_price > prices[index]:
            buy_price = prices[index]
        profit = prices[index] - buy_price
        if profit > max_profit:
           max_profit = profit 
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
