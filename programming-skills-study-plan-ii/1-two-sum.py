class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}
        for i, v in enumerate(nums):
            complement = target - v
            if complement in idx_map:
                return [idx_map[complement], i]
            idx_map[v] = i