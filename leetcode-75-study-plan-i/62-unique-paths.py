class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range (m)]
        
        # Setup dp base case
        for i in range(n):
            dp[0][i] = 1
        for j in range(m):
            dp[j][0] = 1
        
        # Perform dp algorithm
        for j in range(1, n):
            for i in range(1, m):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        
        return dp[-1][-1]