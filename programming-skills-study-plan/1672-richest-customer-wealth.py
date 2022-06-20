from functools import reduce

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        highest = 0
        for account in accounts:
            wealth = reduce(lambda a, b: a + b, account)
            highest = max(wealth, highest)
        return highest