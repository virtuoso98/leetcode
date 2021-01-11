# acceptable, but O(n^2) time complexity

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums), 1):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
                
# alternative solution: using dictionaries because of quicker lookup times. O(n) time complexity

    def twoSum_v1 (self, nums: List[int], target: int) -> List[int]:
            dictionary = {}
    
            for i in range(len(nums)):
                secondNumber = target - nums[i]
                if secondNumber in dictionary.keys():
                    secondIndex = nums.index(secondNumber)
                    if (i != secondIndex): 
                        return sorted([i, secondIndex])

                dictionary.update({nums[i]: i})