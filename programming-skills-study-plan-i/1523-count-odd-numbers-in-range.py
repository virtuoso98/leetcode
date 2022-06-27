class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Just some number counting, I guess...?
        if low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2
        return (high - low) // 2 + 1