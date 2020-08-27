class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        acc = 0
        for i in range(len(nums)):
            acc += nums[i]
            output.append(acc)
        return output
    
    def runningSum_v1(self, nums: List[int]) -> List[int]:
        array = []    
        for index, element in enumerate(nums):
            if index == 0:
                array.append(element)
            else:
                array.append(element + array[index - 1])
        return array

    def runningSum_v2(self, nums: List[int]) -> List[int]:
        array = [nums[0]]
        for index, element in enumerate(nums[1:]):
            array.append(element + array[index])
        return array