class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                # Add 1 to indexes to compensate for 1-indexing
                return [l + 1, r + 1]
            elif total < target:
                l += 1
            else:
                r -= 1