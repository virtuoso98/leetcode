class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        
        for i in range(1, len(nums)):
            left[i] = nums[i - 1] * left[i - 1]
        
        for j in reversed(range(len(nums) - 1)):
            right[j] = nums[j + 1] * right[j + 1]
         
        output = []
        for k in range(len(nums)):
            output.append(right[k] * left[k])

        return output