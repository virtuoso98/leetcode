class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # s for last-seen non-zero, i for fast pointer
        s = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[s], nums[i] = nums[i], nums[s]
                s += 1