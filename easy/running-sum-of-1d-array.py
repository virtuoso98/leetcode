class Solution:
    
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        acc = 0
        for i in range(len(nums)):
            acc += nums[i]
            output.append(acc)
        return output
