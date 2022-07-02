class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for i, v in enumerate(nums):
            if leftSum == total - v:
                return i
            leftSum += v
            total -= v
        return -1