class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Super hack method that makes use of equal length of bijection
        return len(set(s)) == len(set(t)) == len(set(list(zip(s, t))))
        