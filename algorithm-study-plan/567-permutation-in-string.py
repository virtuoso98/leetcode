class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        UNICODE_SHIFT = 97
        a1 = [0] * 26
        a2 = [0] * 26
        l1 = len(s1)
        
        # Setup character frequency array a1
        for c in s1:
            idx = ord(c) - UNICODE_SHIFT
            a1[idx] += 1
        
        for i in range(len(s1) - 1, len(s2)):
            # Setup the array of character frequency
            if i == l1 - 1:
                for j in range(l1):
                    idx = ord(s2[j]) - UNICODE_SHIFT
                    a2[idx] += 1
            
            # Add and remove character based on sliding window
            else:
                add = ord(s2[i]) - UNICODE_SHIFT
                remove = ord(s2[i - l1]) - UNICODE_SHIFT
                a2[add] += 1
                a2[remove] -= 1
            
            # Check for equivalence
            if a1 == a2:
                return True
        return False