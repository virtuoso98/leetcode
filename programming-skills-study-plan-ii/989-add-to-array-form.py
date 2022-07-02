class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # Sorry, I really couldn't be bothered to do this.
        string = ""
        for i in num:
            string += str(i)
        
        res = int(string) + k
        output = list(str(res))
        return output