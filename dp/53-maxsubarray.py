class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        high = float('-inf')
        
        for i in range(len(nums)):
            num = nums[i]
            curr = max(num, curr + num)
            high = max(high, curr)
            
        return high