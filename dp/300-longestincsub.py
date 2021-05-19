class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        
        dp = [0] * len(nums)
        dp[0] = 1
        maxsub = 1
        
        for i in range(1, len(nums)):
            maxval = 0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    maxval = max(maxval, dp[j])
            dp[i] = maxval + 1
            maxsub = max(maxsub, dp[i])
        
        return maxsub