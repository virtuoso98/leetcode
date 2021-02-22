class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if k == 1:
            return nums
        out = []
        for i in range(len(nums) - k + 1):
            temp = sorted(nums[i:(i + k)])
            if k % 2 == 1:
                out.append(temp[k//2])
            else:
                out.append((temp[k//2] + temp[k//2 - 1]) * 0.5)
        return out