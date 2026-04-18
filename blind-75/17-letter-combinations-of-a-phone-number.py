class Solution:
    def backtrack(self, combi, ptr, output, digits, digit_map) -> None:
            if ptr == len(digits):
                output.append(combi)
                return
            for c in digit_map[digits[ptr]]:
                self.backtrack(combi + c, ptr + 1, output, digits, digit_map)

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
        self.backtrack("", 0, output, digits, digit_map)
        return output