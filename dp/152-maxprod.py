class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        low = nums[0]
        high = nums[0]
        final = high
        
        for i in range(1, len(nums)):
            temp = high
            high = max(nums[i], high * nums[i], low * nums[i])
            low = min(nums[i], temp * nums[i], low * nums[i])
            final = max(final, high)
            
        return final