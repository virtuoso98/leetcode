class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        acc = 0
        for i in nums:
            acc += i
        
        l = len(nums)
        total = (l * (l + 1)) // 2
        
        return total - acc