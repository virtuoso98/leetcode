class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [cost[0], cost[1]]
        l = len(cost)
        if l < 3:
            return dp[1]
        else:
            for i in range (2, l):
                dp.append(cost[i] + min(dp[i - 1], dp[i - 2]))
        
        return min(dp[l - 1], dp[l - 2])