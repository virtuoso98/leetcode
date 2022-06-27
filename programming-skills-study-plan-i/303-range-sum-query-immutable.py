class NumArray:

    def __init__(self, nums: List[int]):
        dp = [0 for _ in range(len(nums) + 1)]
        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] + nums[i - 1]
        self.dp = dp

    def sumRange(self, left: int, right: int) -> int:
        # Use culminative sum to make calculation O(1)
        return self.dp[right + 1] - self.dp[left]