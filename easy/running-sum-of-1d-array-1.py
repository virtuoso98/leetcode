class Solution:
    
    def runningSum_v1(self, nums: List[int]) -> List[int]:
        array = []    
        for index, element in enumerate(nums):
            if index == 0:
                array.append(element)
            else:
                array.append(element + array[index - 1])
        return array
