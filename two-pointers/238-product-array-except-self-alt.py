class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        
        for i in range(1, len(nums)):
            ans[i] = nums[i - 1] * ans[i - 1]
        
        right = 1
        
        for j in reversed(range(len(nums))):
            ans[j] *= right
            right *= nums[j]
            
        return ans