class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            # Update minimum price
            min_price = min(min_price, price)
            # Update current maximum profit
            profit = price - min_price
            max_profit = max(profit, max_profit)
        return max_profit