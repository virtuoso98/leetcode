class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0 if i == 0 else amount+1 for i in range(amount+1)]
        for i in range(amount+1):
            for coin in coins:
                prev = i - coin
                if prev >= 0 and dp[prev] < amount:
                    dp[i] = min(dp[i], dp[prev] + 1)
        print(dp)
        return -1 if dp[amount] > amount else dp[amount] 