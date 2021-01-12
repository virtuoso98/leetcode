class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        
        # don't do this - rows and columns point to same 
        # location in memory
        # dp = [[0] * (len1 + 1)] * (len2 + 1)
        
        dp = [[0 for i in range(len1 + 1)] for i in range (len2 + 1)]
        
        for i in range (0, len1 + 1):
            dp[0][i] = i
        
        for j in range (0, len2 + 1):
            dp[j][0] = j
            
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                left = dp[j][i - 1]
                up = dp[j - 1][i]
                diag = dp[j - 1][i - 1]
                if word1[i - 1] == word2[j - 1]:
                    dp[j][i] = 1 + min(left, up, diag - 1)
                else: 
                    dp[j][i] = 1 + min(left, up, diag)
        
        return dp[len2][len1]