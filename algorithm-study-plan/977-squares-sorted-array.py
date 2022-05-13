class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        res = [0] * len(nums)
        for i in range(r, -1, -1):
            absL = abs(nums[l])
            absR = abs(nums[r])
            if absL > absR:
                res[i] = absL ** 2
                l += 1
            else:
                res[i] = absR ** 2
                r -= 1
                
        return res