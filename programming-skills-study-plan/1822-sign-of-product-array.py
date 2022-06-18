from functools import reduce

class Solution:
    def preserveSign(self, num):
        if num > 0:
            return 1
        if num < 0:
            return -1
        # Since number already 0
        return 0
    
    def arraySign(self, nums: List[int]) -> int:
        nums = map(self.preserveSign, nums)
        return reduce(lambda a, b: a * b, nums)