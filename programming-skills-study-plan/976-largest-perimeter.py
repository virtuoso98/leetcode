class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Sort in descending order
        nums.sort(reverse = True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i + 2] + nums[i + 1] + nums[i]
        return 0