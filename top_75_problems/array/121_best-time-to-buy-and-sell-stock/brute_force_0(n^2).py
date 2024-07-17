from typing import List


def maxProfit(prices: List[int]) -> int:
    """
    Check every pair of days (buy day and sell day) and calculate profit and store max_profit.
        If current profit is greater than max_profit - update max_profit.
    Time complexity: 0(n^2), two times itteration.
    Space Complexity: 0(1), store a constant.
    """
    days = len(prices)
    max_profit = 0

    for buy_day in range(days):
        for sell_day in range(buy_day + 1, days):
            profit = prices[sell_day] - prices[buy_day]
            if profit > max_profit:
                max_profit = profit

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
