class Solution:
                
    def findRightMost(self, nums, target) -> int:
        r = len(nums) - 1
        l = 0
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                ans = mid
                if ans == len(nums) - 1 or nums[ans] != nums[ans + 1]:
                    return ans
                else:
                    l = mid + 1
            if nums[mid] > target:
                r = mid - 1
            if nums[mid] < target:
                l = mid + 1
                
        return -1
    

    def findLeftMost(self, nums, target) -> int:
        r = len(nums) - 1
        l = 0
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                ans = mid
                if ans == 0 or nums[ans] != nums[ans - 1]:
                    return ans
                else:
                    r = mid - 1
            if nums[mid] > target:
                r = mid - 1
            if nums[mid] < target:
                l = mid + 1
                
        return -1        
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        r = self.findRightMost(nums, target)
        l = self.findLeftMost(nums, target)
        return [l, r]
        