class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        neg_placeholder = ""
        if x < 0:
            neg_placeholder = "-"
        
        strn = str(abs(x))
        while strn[-1] == "0":
            strn = strn[0: len(strn) - 1]
        
        temp = strn[::-1]
        temp1 = int(neg_placeholder + temp)
        if temp1 < - (2 ** 31) or temp1 > 2 ** 31 - 1:
            return 0
        else:
            return int(neg_placeholder + temp)
        