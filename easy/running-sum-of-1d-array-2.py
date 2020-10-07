class Solution:

    def runningSum_v2(self, nums: List[int]) -> List[int]:
        array = [nums[0]]
        for index, element in enumerate(nums[1:]):
            array.append(element + array[index])
        return array