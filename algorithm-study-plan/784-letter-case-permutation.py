class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        arr = [[]]
        for c in s:
            n = len(arr)
            if c.isalpha():
                for i in range(n):
                    # Create new duplicate entry. 2 Permutations here
                    arr.append(arr[i][:])
                    # Append lower and upper case
                    arr[i].append(c.upper())
                    arr[i + n].append(c.lower())
            else:
                for i in range(n):
                    arr[i].append(c)
                
        ans = map("".join, arr)
        return ans