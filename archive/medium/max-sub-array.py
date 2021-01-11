class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        self.local_max = 0 
        global_max = float("-inf")
        
        # kadane's algorithm
        for i in range(length) :
            self.local_max = max(nums[i], nums[i] + self.local_max)
            
            if self.local_max > global_max : 
                global_max = self.local_max
                
        return global_max
