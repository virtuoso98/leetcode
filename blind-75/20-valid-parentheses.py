class Solution:
    def isValid(self, s: str) -> bool:
        pair_map = {")": "(",
            "}": "{",
            "]": "["
        }
        stk = []
        for c in s:
            if c in pair_map.values():
                stk.append(c)
            else:
                if len(stk) == 0:
                    return False
                comp = pair_map[c]
                if comp != stk.pop():
                    return False
        return len(stk) == 0