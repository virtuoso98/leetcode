class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str_builder = []
        l1, l2 = len(word1), len(word2)
        
        # Alternating concatenation
        for i in range(max(l1, l2)):
            if i < l1:
                str_builder.append(word1[i])
            if i < l2:
                str_builder.append(word2[i])
                
        return "".join(str_builder) 