class Solution:
    def factorial(self, n: int) -> int:
        if n == 0: 
            return 1
        return self.factorial(n - 1) * n
    def uniquePaths(self, m: int, n: int) -> int:
        return self.factorial(m + n -2) // (self.factorial(m - 1) * self.factorial(n - 1))