class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # Not so cringe poggers solution
        ans = 0
        n = len(arr)
        for i, v in enumerate(arr):
            # Number of subarrays ending with current idx
            nl = i + 1
            # Number of subarrays starting with current idx
            nr = n - i
            # nl * nr gives total combination of subarrays containing idx
            # Number of odd length subarrays would then be half of this, rounded up
            ans += math.ceil((nl * nr + 1) // 2) * v
        return ans