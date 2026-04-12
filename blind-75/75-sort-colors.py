class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Dutch national flag algo
        r = 0
        w = 0
        b = len(nums) - 1
        while w <= b:
            v = nums[w]
            if v == 0:
                nums[r], nums[w] = nums[w], nums[r]
                w += 1
                r += 1
            elif v == 2:
                nums[b], nums[w] = nums[w], nums[b]
                b -= 1
            else: # v == 1
                w += 1           
        