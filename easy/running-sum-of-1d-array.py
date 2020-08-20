class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        acc = 0
        for i in range(len(nums)):
            acc += nums[i]
            output.append(acc)
        return output
    

class Solution2:
    array = []
    def runningSum(self, nums: List[int]) -> List[int]:
        for index, element in enumerate(nums):
            if index == 0:
                array.append(element)
            else:
                array.append(element + array[index - 1])
        return array


class Solution3:
    def runningSum(self, nums: List[int]) -> List[int]:
        array = [nums[0]]
        for index, element in enumerate(nums[1:]):
            array.append(element + array[index])
        return array