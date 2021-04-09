class Solution:
    def threeSumAux(self, nums, lo, acc):
        l = lo + 1
        r = len(nums) - 1
        while l < r:
            total = nums[lo] + nums[l] + nums[r]
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                acc.append([nums[lo], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
        
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        acc = []
        if len(nums) < 3: 
            return acc
        
        for lo in range(len(nums) - 2):
            if nums[lo] > 0:
                break
            # important to prevent repetition
            if lo == 0 or nums[lo - 1] != nums[lo]:
                self.threeSumAux(nums, lo, acc)
        
        return acc
        