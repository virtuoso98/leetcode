class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        glob = set(nums)
        seen = set()
        max_res = 0
        for num in nums:
            if num in seen:
                continue # already traversed, no need to do again
            
            curr_num = num
            while curr_num - 1 in glob:
                curr_num -= 1 # Navigate to the lowest number in the set
            
            curr_res = 0 # count all the way to the last number
            while curr_num in glob:
                seen.add(curr_num)
                curr_res += 1
                curr_num += 1
            max_res = max(max_res, curr_res)
        return max_res
        