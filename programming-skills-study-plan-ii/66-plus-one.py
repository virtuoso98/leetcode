class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            # Reset to 0 since addition carried to next digit
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                break
                
        # If all digits are 9, then need to add new digit
        if i < 0:
            return [1] + digits
        else:
            digits[i] += 1
            return digits