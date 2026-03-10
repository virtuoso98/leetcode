class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            ans = max(ans, w * h)
            if h == height[r]:
                r -= 1
            else:
                l += 1
        return ans