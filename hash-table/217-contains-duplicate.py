class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table = set()
        for i in range(len(nums)):
            if nums[i] not in table:
                table.add(nums[i])
            else:
                return True
        return False