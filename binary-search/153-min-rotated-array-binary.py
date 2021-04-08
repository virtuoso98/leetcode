class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        if nums[r] >= nums[0]:
            return nums[0]
        
        while l < r:
            mid = (r - l) // 2 + l
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1