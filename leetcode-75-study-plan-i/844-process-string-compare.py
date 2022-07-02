class Solution:
    def processString(self, f: str) -> str:
        stk = []
        for c in f:
            if c != "#":
                stk.append(c)
            elif len(stk) != 0:
                stk.pop()
                
        return "".join(stk)
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.processString(s) == self.processString(t)