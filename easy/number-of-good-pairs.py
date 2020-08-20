class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dict = {}
        acc = 0 
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        for k, v in dict.items():
            acc += (v - 1) / 2 * v
        
        return int(acc)