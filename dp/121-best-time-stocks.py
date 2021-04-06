class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        high = 0
        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
            elif prices[i] - low > high:
                high = prices[i] - low
        return high
        