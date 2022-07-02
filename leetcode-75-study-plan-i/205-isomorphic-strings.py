class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = dict()
        t_to_s = dict()
        for i, j in list(zip(s, t)):
            if i not in s_to_t and j not in t_to_s:
                s_to_t[i] = j
                t_to_s[j] = i
            # This works because default value is None
            elif s_to_t.get(i) != j or t_to_s.get(j) != i:
                return False
        return True