class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            heightL = height[l]
            heightR = height[r]
            vol = min(heightL, heightR) * (r - l)
            res = max(res, vol)            
            if heightL > heightR:
                r -= 1
            else:
                l += 1
        return res