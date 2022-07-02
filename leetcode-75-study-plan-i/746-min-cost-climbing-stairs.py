class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # i-th step added by minimum of last 2
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
            
        # Minimum of last 2 steps
        return min(cost[-1], cost[-2])