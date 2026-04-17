class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                dp[i] = max(dp[i], dp[j] + 1 if nums[i] > nums[j] else 0)
        return max(dp)