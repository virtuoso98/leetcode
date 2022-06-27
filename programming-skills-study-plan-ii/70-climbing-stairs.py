class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        first, second = 1, 2
        for _ in range(2, n):
            tmp = second
            second = first + second
            first = tmp
        
        return second