class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n_diff = 0
        s1_diff = set()
        s2_diff = set()
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                n_diff += 1
                s1_diff.add(s1[i])
                s2_diff.add(s2[i])
        return n_diff == 0 or (n_diff == 2 and s1_diff == s2_diff)