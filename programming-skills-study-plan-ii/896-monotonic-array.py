class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        """No point doing 1 pass. Still doing 2 comparisons per iteration"""
        is_monotone_decreasing = all(
            nums[i] >= nums[i + 1] for i in range(len(nums) - 1)
        )
        is_monotone_increasing = all(
            nums[i] <= nums[i + 1] for i in range(len(nums) - 1)
        )
        
        return is_monotone_decreasing or is_monotone_increasing