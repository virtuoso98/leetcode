class Solution:
    def backtrack(combi, ptr) -> None:
            if ptr == len(digits):
                output.append(combi)
                return
            for c in digit_map[digits[ptr]]:
                backtrack(combi + c, ptr + 1)

    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        output = []
        backtrack("",0, output)
        return output