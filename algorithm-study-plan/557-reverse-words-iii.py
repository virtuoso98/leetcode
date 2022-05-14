class Solution:
    def reverseWord(self, w: str) -> str:
        a = list(w)
        l = 0
        r = len(a) - 1
        while l < r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
        return "".join(a)
    
    def reverseWords(self, s: str) -> str:
        word_arr = s.split(" ")
        rev_word_arr = map(self.reverseWord, word_arr)
        return " ".join(rev_word_arr)